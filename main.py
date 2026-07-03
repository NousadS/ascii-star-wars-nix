"""
Playing ASCII Art (Star Wars) from https://www.asciimation.co.nz/
"""

import asyncio
from pathlib import Path
import sys

STARWARS_FILE: Path = Path().cwd() / "starwars.txt"


async def main() -> None:
    lines_per_frame: int = 14  # includes delay line + frame lines

    if not STARWARS_FILE.exists():
        raise FileNotFoundError(f"[!] File {STARWARS_FILE.name} does not exist. ({STARWARS_FILE.resolve()})")

    print("[*] Loading animation file...")

    data: list[str] = STARWARS_FILE.read_text(encoding="utf-8").splitlines()

    print(f"[+] Loaded {len(data)} lines")

    # Initial spacing for terminal rendering
    print("\n" * lines_per_frame)

    for frame_start in range(0, len(data), lines_per_frame):
        frame_block: list[str] = data[frame_start : frame_start + lines_per_frame]
        delay_line: str = frame_block[0]
        frame_lines: list[str] = frame_block[1:]

        # Clear terminal (more standard sequence)
        print("\033[2J\033[H", end="")
        print("\n".join(frame_lines))

        try:
            delay_ms: int = int(delay_line)

            await asyncio.sleep(delay_ms * 67 / 1000)
        except ValueError:
            # delay_ms:int  = 0
            continue


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass