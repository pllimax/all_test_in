import socket, json

results = {}
host = "frp-six.com"

# 测试 frp 常用端口
ports = [80, 443, 7000, 7001, 7500, 8080, 8443, 40752, 40000, 50000, 60000]

for port in ports:
    try:
        s = socket.create_connection((host, port), timeout=3)
        results[f"{host}:{port}"] = "OK"
        s.close()
    except Exception as e:
        results[f"{host}:{port}"] = str(e)

for k, v in results.items():
    status = "OK" if v == "OK" else "FAIL"
    print(f"  [{status}] {k}")

# 对通的端口，尝试发送 frp 登录消息验证是否是 frp 服务器
import struct, json as j, time, uuid

for port in [80, 443]:
    try:
        s = socket.create_connection((host, port), timeout=5)
        login = {
            "version": "0.69.1",
            "hostname": socket.gethostname(),
            "os": "windows",
            "arch": "amd64",
            "privilege_key": "9r77q7ew83d91ue4v14805isyhdsqlcb",
            "timestamp": int(time.time()),
            "run_id": uuid.uuid4().hex[:16],
            "pool_count": 1,
        }
        content = j.dumps(login, separators=(",", ":")).encode()
        header = struct.pack(">Bq", ord("o"), len(content))
        s.sendall(header + content)
        s.settimeout(3)
        resp = s.recv(1024)
        if resp:
            type_byte = resp[0]
            print(f"  frp检测 {host}:{port} -> 收到响应! 类型: {chr(type_byte)} (0x{type_byte:02x})")
            print(f"  原始数据: {resp[:200].hex()}")
        else:
            print(f"  frp检测 {host}:{port} -> 无响应")
        s.close()
    except Exception as e:
        print(f"  frp检测 {host}:{port} -> {e}")

with open("net_diag2.json", "w") as f:
    j.dump(results, f, indent=2)
print("\n完成")