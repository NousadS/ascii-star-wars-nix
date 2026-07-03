# ASCIIStarWars (Python)

Renewed version of the original player script, now complemented by an updater script.

> Original description from Matija Gračanin (mgracanin)

If you're missing ASCII Star Wars via telnet at towel.blinkenlights.nl, this will play the same thing in Python terminal directly. 

This program plays the Star Wars movie in ASCII art in the Python terminal. Was thinking calling it Python Wars, but it just didn't seem quite right. So, I've named it ASCIIStarWars. There are no special requirements, except that you have starwars.txt file which you can also find in this repository.

> [!NOTE] 
> The player script has no external dependencies.
> The updater script requires the `requests` package.
> See [Usage](#usage).

# Usage

There is two ways to use this repository either as a **Nix flake** or as pure **Python scripts**.

---

The first script is [`main.py` or the player](main.py). It will play the Star Wars movie in ASCII art in your terminal. Just make sure you have the `starwars.txt` file in the same directory where you run the command. To run the script you can either use nix flake or just python:

```bash
# Nix
nix run .#

# Python
python main.py
```

---

The second script is [`update.py` or the updater](update.py). The updater downloads the latest ASCII Star Wars animation from **asciimation.co.nz** to `starwars.txt`, preserving the last file as an archive. To run the script you have both previous options:

> [!WARNING]
> If this script is used with pure python, please ensure the `requests` package
> or it would fail to run! If used as a nix flake this package is being installed automatically.

```bash
# Nix
nix run .#update

# Python
python update.py
```

## Data source

The ASCII animation is originally from:

* www.asciimation.co.nz/

You can learn more about the format here:

* www.asciimation.co.nz/asciimation/ascii_faq.html

## Credits

The ASCII art used in this program was originally created by ***Simon Jansen***. I would like to thank him for his amazing work that is still popular (and amazing) to this day.

The original Python player was written by [***Matija Gračanin (mgracanin)***](https://github.com/mgracanin), on which this version is based.

## License

This program is licensed under the **MIT License** - see [LICENSE](LICENSE)
