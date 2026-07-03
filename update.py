"""
Updating ASCII Art (Star Wars) from https://www.asciimation.co.nz/
"""

import re
import requests
from pathlib import Path
import shutil
from datetime import datetime
from typing import Optional, Pattern, Match

STARWARS_FILE: Path = Path().cwd() / "starwars.txt"
URL: str = "https://www.asciimation.co.nz/"
FILM_REGEX: Pattern[str] = re.compile(r"var film = '(.*)'\.split")

print(f"[*] Getting new film from {URL}")

response = requests.get(URL, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
})

if response.status_code != 200:
    raise RuntimeError(f"[!] Error connecting to {URL} ({response.status_code})")
else:
    print(f"[+] Successfully fetched page ({response.status_code})")


print("[*] Extracting film data from HTML")

result: Optional[Match[str]] = FILM_REGEX.search(response.text)

if not result:
    raise RuntimeError("[!] Could not find film data in page source")

film_text: str = result.group(1)

# Javascript escaping
film_text = film_text.replace(r"\n", "\n")
film_text = film_text.replace(r"\\", "\\") # Yes that works
film_text = film_text.replace(r"\'", "'")
film_text = film_text.replace(r"\"", '"')

old_size: Optional[int] = None
new_size: int = len(film_text.encode("utf-8"))

if STARWARS_FILE.exists():
    print("[*] Existing file found")

    old_film_text: str = STARWARS_FILE.read_text(encoding="utf-8")

    print("[*] Extracting archive year from existing file")

    year_match: Optional[Match[str]] = re.search(
        r"Simon Jansen.*?(\d{4})\s*$",
        old_film_text,
        re.MULTILINE,
    )

    archive_year: str = f"fallback_{datetime.now().year}"

    if not year_match:
        print("[!] Could not extract archive year, using fallback")
    else:
        archive_year = year_match.group(1)

    archive_path: Path = STARWARS_FILE.with_name(f"starwars_{archive_year}.txt")

    print(f"[*] Archiving old file as {archive_path.name}")

    shutil.copy2(STARWARS_FILE, archive_path)

    print("[+] Archive created successfully")

    old_size = STARWARS_FILE.stat().st_size

    print(f"[*] Size comparison (bytes)")
    print(f"    - Old: {old_size}")
    print(f"    - New: {new_size}")
    print(f"    - Diff: {new_size - old_size:+}")
else:
    print("[*] No existing file found, creating new one")
    print(f"[*] New file size: {new_size} bytes")

STARWARS_FILE.write_text(film_text, encoding="utf-8")

print(f"[+] Wrote new film data to {STARWARS_FILE.name}")
