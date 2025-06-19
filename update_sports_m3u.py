import requests

M3U_URL = "https://raw.githubusercontent.com/yang-1989/IPTV/main/migu/migu.m3u"
KEYWORDS = ["咪咕", "腾讯", "CBA", "NBA", "英超", "网球", "体育"]
OUTPUT_FILE = "sports_playlist.m3u"

def fetch_and_filter_m3u():
    print(f"正在请求直播源：{M3U_URL}")
    res = requests.get(M3U_URL)
    res.encoding = 'utf-8'

    lines = res.text.splitlines()
    filtered_lines = []

    for i, line in enumerate(lines):
        if any(keyword in line for keyword in KEYWORDS):
            filtered_lines.append(line)
            if i + 1 < len(lines):
                filtered_lines.append(lines[i + 1])

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        f.write("\n".join(filtered_lines))

    print(f"已生成 {OUTPUT_FILE}，共 {len(filtered_lines) // 2} 个频道")

if __name__ == "__main__":
    fetch_and_filter_m3u()
