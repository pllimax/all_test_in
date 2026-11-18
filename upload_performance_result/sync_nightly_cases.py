"""nightly 用例自动同步（增量追加，只增不删）。

每日 12:00 由 GitHub Actions（.github/workflows/nightly-testcases-sync.yml）运行：
扫描社区 sgl-project/sglang main 上注册到 nightly suite / 多机 matrix 的用例，把
testcases_config.json 中缺失的用例以 {source: "nightly", type: ...} 追加进去并提交
到 Gitee；服务器现有的 10 分钟 git fetch + merge --ff-only cron 会自动下发到线上，
无需人工同步。

设计约束：
  - 只增不删：社区已下线的用例、类型差异仅写入报告，人工确认后再改，避免误删
    手工维护条目（images 字段等）
  - 单次新增超过阈值（默认 30）视为上游异常（目录重构/批量误注册），直接失败
    退出且不落盘
  - 不在服务器上运行本脚本：服务器直接改 git 管理文件会破坏 10 分钟 fast-forward
    同步链路

用法：python3 sync_nightly_cases.py [--repo-dir PATH] [--config PATH]
                                   [--report-dir PATH] [--max-add N] [--dry-run] [--no-fetch]
"""
import argparse
import json
import os
import sys
from datetime import datetime, timedelta

from check_testcases_drift import (
    DEFAULT_REPO,
    FETCH_TIMEOUT,
    NIGHTLY_REPO,
    load_nightly_suites,
    run_git,
    scan_registered_cases,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = os.path.join(BASE_DIR, "testcases_config.json")
DEFAULT_REPORT_DIR = os.path.join(DEFAULT_REPO, "logs", "testcases_drift")
DEFAULT_MAX_ADD = 30


def _write_report(report_dir, text):
    """报告落到 logs/testcases_drift/（git-ignored），与漂移检测报告同目录。"""
    os.makedirs(report_dir, exist_ok=True)
    now = datetime.now()
    for name in (f"sync-{now:%Y%m%d}.txt", "sync-latest.txt"):
        path = os.path.join(report_dir, name)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        os.replace(tmp, path)
    cutoff = f"sync-{(now - timedelta(days=30)):%Y%m%d}"
    for name in os.listdir(report_dir):
        if name.startswith("sync-") and name != "sync-latest.txt" and name < cutoff:
            try:
                os.remove(os.path.join(report_dir, name))
            except OSError:
                pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-dir", default=NIGHTLY_REPO,
                    help="社区 sglang 克隆路径（默认 .testcases_repo/nightly）")
    ap.add_argument("--config", default=DEFAULT_CONFIG,
                    help="testcases_config.json 路径")
    ap.add_argument("--report-dir", default=DEFAULT_REPORT_DIR)
    ap.add_argument("--max-add", type=int, default=DEFAULT_MAX_ADD,
                    help="单次允许新增的最大用例数，超过则视为上游异常并退出")
    ap.add_argument("--dry-run", action="store_true", help="只输出差异，不写配置")
    ap.add_argument("--no-fetch", action="store_true", help="跳过社区仓 fetch")
    args = ap.parse_args()

    now = datetime.now()
    lines = [
        f"nightly 用例自动同步  {now:%Y-%m-%d %H:%M:%S}",
        f"社区仓: {args.repo_dir}",
        f"平台配置: {args.config}",
    ]

    def finish(code, extra_lines=()):
        lines.extend(extra_lines)
        text = "\n".join(lines)
        print(text)
        _write_report(args.report_dir, text)
        return code

    if not args.no_fetch:
        rc, _out, err = run_git(args.repo_dir, ["fetch", "origin", "main"],
                                timeout=FETCH_TIMEOUT)
        if rc != 0:
            return finish(1, [f"[错误] 社区仓 fetch 失败: {err.strip()[:300]}"])
        rc, _out, err = run_git(args.repo_dir, ["merge", "--ff-only", "FETCH_HEAD"])
        if rc != 0:
            return finish(1, [f"[错误] 社区仓 fast-forward 失败: {err.strip()[:300]}"])

    head_rc, head, _ = run_git(args.repo_dir, ["rev-parse", "--short", "HEAD"])
    lines.append(f"社区仓 HEAD: {head.strip() if head_rc == 0 else '未知'}")

    suites = load_nightly_suites(args.repo_dir)
    lines.append(f"nightly suite 数: {len(suites)}")
    if not suites:
        return finish(1, ["[错误] 未能提取 nightly suite，社区仓克隆可能不完整"])

    registered = scan_registered_cases(args.repo_dir, suites)
    lines.append(f"社区 nightly 注册用例数: {len(registered)}")

    try:
        with open(args.config, encoding="utf-8") as f:
            cfg = json.load(f)
    except Exception as e:
        return finish(1, [f"[错误] 读取平台配置失败: {e}"])
    lines.append(f"平台配置用例数: {len(cfg)}")

    missing = sorted(set(registered) - set(cfg))
    extra = [c for c in sorted(set(cfg) - set(registered))
             if "fulltest" not in cfg[c].get("source", "")]
    type_diff = [(c, cfg[c].get("type"), registered[c]["type"])
                 for c in sorted(set(registered) & set(cfg))
                 if cfg[c].get("type") != registered[c]["type"]]

    if not missing:
        return finish(0, ["结论: 无新增用例，配置已是最新。"])

    if len(missing) > args.max_add:
        return finish(2, [
            f"[错误] 单次新增 {len(missing)} 条，超过阈值 {args.max_add}，"
            "疑似上游异常，未写入配置。请人工核对后处理：",
        ] + [f"  + {c}  type={registered[c]['type']}" for c in missing])

    added = {c: {"source": "nightly", "type": registered[c]["type"]} for c in missing}
    if args.dry_run:
        return finish(0, [f"[dry-run] 将新增 {len(added)} 条，未写入配置。"]
                      + [f"  + {c}  type={added[c]['type']}" for c in missing])

    cfg.update(added)
    tmp = args.config + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, args.config)

    report = [f"结论: 已新增 {len(added)} 条用例（配置总数 {len(cfg)}）。"]
    report += [f"  + {c}  type={added[c]['type']}" for c in missing]
    if extra:
        report.append(f"\n== 多余 {len(extra)} 条（仅提示，未自动删除）==")
        report += [f"  - {c}  source={cfg[c].get('source')}" for c in extra]
    if type_diff:
        report.append(f"\n== 类型差异 {len(type_diff)} 条（仅提示，未自动修改）==")
        report += [f"  ! {c}: config={have} community={want}"
                   for c, have, want in type_diff]
    return finish(0, report)


if __name__ == "__main__":
    sys.exit(main())
