import json
from datetime import datetime

def build():
    with open("data/alive.txt") as f:
        proxies = [i.strip() for i in f if i.strip()]

    data = {
        "updated": datetime.utcnow().isoformat(),
        "count": len(proxies),
        "type": "socks5",
        "country": "TW",
        "proxies": proxies
    }

    with open("data/alive.json", "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print("[+] 代理池已生成")


if __name__ == "__main__":
    build()
