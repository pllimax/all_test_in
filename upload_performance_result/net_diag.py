import socket, json, sys

results = {}

# 1. DNS 解析测试
hosts = [
    "frp-six.com",
    "cn-zz-bgp-1.natfrp.cloud", 
    "www.baidu.com",
    "www.natfrp.com",
    "github.com",
]
for host in hosts:
    try:
        ip = socket.gethostbyname(host)
        results[f"DNS:{host}"] = ip
    except Exception as e:
        results[f"DNS:{host}"] = f"FAIL: {e}"

# 2. 端口连通性测试
tests = [
    ("frp-six.com", 7000),
    ("frp-six.com", 80),
    ("frp-six.com", 443),
    ("frp-six.com", 40752),
    ("www.baidu.com", 80),
    ("www.baidu.com", 443),
    ("www.natfrp.com", 443),
    ("cn-zz-bgp-1.natfrp.cloud", 7000),
]

for host, port in tests:
    try:
        s = socket.create_connection((host, port), timeout=4)
        results[f"TCP:{host}:{port}"] = "OK"
        s.close()
    except Exception as e:
        results[f"TCP:{host}:{port}"] = str(e)

# 3. 输出
for k, v in results.items():
    print(f"  {k}: {v}")

# 保存到文件
with open("net_diag.json", "w") as f:
    json.dump(results, f, indent=2)
print("\n结果已保存到 net_diag.json")