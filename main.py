from wordle_helper import WordleHelper

def main():
    helper = WordleHelper('data/russian.txt')

    green_input = input("Enter green letters (e.g., _о___): ")
    green = {i: ch for i, ch in enumerate(green_input) if ch != '_'}

    yellow_input = input("Enter yellow letters with positions (e.g., с:0 л:2): ")
    yellow_letters = {}
    if yellow_input.strip():
        for entry in yellow_input.split():
            letter, pos = entry.split(':')
            yellow_letters.setdefault(letter, []).append(int(pos))

    grey_input = input("Enter grey letters (not in the word): ")

    helper.filter_green(green)
    helper.filter_yellow(yellow_letters)
    helper.filter_grey(grey_input)

    print("\nPossible word candidates:")
    print(helper.get_candidates())

if __name__ == "__main__":
    main()
