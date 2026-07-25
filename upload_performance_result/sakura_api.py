"""
通过 Sakura Frp API 获取隧道和节点信息
"""
import urllib.request
import json
import ssl

token = "9r77q7ew83d91ue4v14805isyhdsqlcb"
ctx = ssl.create_default_context()

# 尝试多个可能的 API 端点
endpoints = [
    # Sakura Frp 可能 API
    "https://www.natfrp.com/api/tunnel/list",
    "https://www.natfrp.com/api/user/tunnels",
    "https://www.natfrp.com/api/v2/tunnels",
    "https://www.natfrp.com/api/node/list",
    "https://www.natfrp.com/api/v2/nodes",
    "https://api.natfrp.com/tunnels",
    "https://api.natfrp.com/v2/tunnels",
    # frp 配置拉取 API
    "https://www.natfrp.com/api/frp/config",
    "https://www.natfrp.com/api/v2/frp/config",
]

for url in endpoints:
    try:
        req = urllib.request.Request(url)
        req.add_header("Authorization", f"Bearer {token}")
        req.add_header("X-Access-Token", token)
        req.add_header("Content-Type", "application/json")
        resp = urllib.request.urlopen(req, timeout=5, context=ctx)
        data = resp.read().decode()
        print(f"[OK] {url}")
        print(f"  响应: {data[:500]}")
        resp.close()
    except urllib.error.HTTPError as e:
        print(f"[{e.code}] {url}")
    except Exception as e:
        print(f"[FAIL] {url}: {e}")

# 尝试直接用 frp 协议拉取配置
print("\n--- 尝试 frp 配置拉取 ---")
import socket
try:
    s = socket.create_connection(("www.natfrp.com", 443), timeout=5)
    # 尝试 HTTP 请求
    request = f"GET /api/frp/config?token={token} HTTP/1.1\r\nHost: www.natfrp.com\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode())
    resp = s.recv(4096).decode(errors="replace")
    print(f"HTTP响应: {resp[:500]}")
    s.close()
except Exception as e:
    print(f"HTTP请求失败: {e}")