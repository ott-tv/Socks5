import requests
import socket
import socks
from concurrent.futures import ThreadPoolExecutor

TEST_URL = "https://httpbin.org/ip"
TIMEOUT = 8
THREADS = 50

def check(proxy):
    try:
        ip, port = proxy.split(":")
        socks.set_default_proxy(socks.SOCKS5, ip, int(port))
        socket.socket = socks.socksocket

        r = requests.get(TEST_URL, timeout=TIMEOUT)
        if r.status_code == 200:
            return proxy
    except:
        return None


if __name__ == "__main__":
    with open("data/raw.txt") as f:
        proxies = [i.strip() for i in f if i.strip()]

    alive = []

    with ThreadPoolExecutor(max_workers=THREADS) as pool:
        for result in pool.map(check, proxies):
            if result:
                print("[OK]", result)
                alive.append(result)

    with open("data/alive.txt", "w") as f:
        for p in alive:
            f.write(p + "\n")

    print(f"[+] 存活代理 {len(alive)} 条")
