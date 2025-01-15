import re

url = input("URL: ").strip()

pattern = r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)"

if matches := re.search(pattern, url, re.IGNORECASE):
    print(f"Username:", matches.group(1))