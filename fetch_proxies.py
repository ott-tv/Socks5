import requests
from bs4 import BeautifulSoup

SOURCES = [
    "https://proxy5.net/cn/free-proxy/taiwan",
    "https://proxyhub.me/zh/tw-socks5-proxy-list.html",
    "https://www.freeproxy.world/?type=socks5&country=TW"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (ProxyPool Bot)"
}

def fetch():
    proxies = set()

    for url in SOURCES:
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            soup = BeautifulSoup(r.text, "html.parser")

            for td in soup.find_all("td"):
                text = td.get_text(strip=True)
                if ":" in text:
                    ip, port = text.split(":", 1)
                    if ip.count(".") == 3 and port.isdigit():
                        proxies.add(f"{ip}:{port}")
        except Exception as e:
            print(f"[!] 抓取失败 {url}: {e}")

    return proxies


if __name__ == "__main__":
    proxies = fetch()
    with open("data/raw.txt", "w") as f:
        for p in sorted(proxies):
            f.write(p + "\n")

    print(f"[+] 抓取完成，共 {len(proxies)} 条")
