# Wordle Solver for Russian 5-letter Words

This is a simple but powerful interactive assistant for solving the Russian version of the game similar to Wordle ("5 букв").

It allows you to filter valid 5-letter words based on:
- **Green letters** – correct letter in the correct position,
- **Yellow letters** – letter is in the word, but in the wrong position,
- **Grey letters** – letter is not in the word.

---

## Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/DimKrav/wordle-solver.git
cd wordle-solver
pip install -r requirements.txt
```

---

## Usage (CLI)
```bash
python main.py
```

Example input:
```text
Enter green letters: _о___
Enter yellow letters with positions: с:0 л:2
Enter grey letters: кенвапрдяиь
```

---

## Always win strategy
1. Start the game with words `сонет`, `вилка`, `прядь`. They contain many common Russian letters. 
2. Enter the hints you get into the CLI (`main.py`).
3. Review the suggestions and choose the most promising word.
4. Repeat until you win!

---

## Data Source
The Russian word list `russian.txt` was sourced from the repository [danakt/russian-words](https://github.com/danakt/russian-words) by [Danakt Saushkin](https://github.com/danakt/).  
- The file contains 1,531,464 Russian words in all inflected forms
- Encoding: Windows‑1251
- License: MIT License

---

## License
This project is licensed under the MIT License.
See the [LICENSE](./LICENSE) file for more details.