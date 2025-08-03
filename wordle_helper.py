import pandas as pd

class WordleHelper:
    def __init__(self, wordlist_path='russian.txt', encoding='windows-1251'):
        self.df = pd.read_csv(wordlist_path, encoding=encoding, header=None)
        self.df.columns = ['word']
        self.df['word'] = self.df['word'].str.replace('-', '')
        self.df = self.df[self.df['word'].str.len() == 5]

    def filter_green(self, known_positions: dict):
        """known_positions: {0: 'с', 2: 'р'}"""
        for pos, char in known_positions.items():
            self.df = self.df[self.df['word'].str[pos] == char]

    def filter_yellow(self, misplaced_letters: dict):
        """misplaced_letters: {'с': [0], 'л': [2]}"""
        for letter, wrong_positions in misplaced_letters.items():
            self.df = self.df[self.df['word'].str.contains(letter)]
            for pos in wrong_positions:
                self.df = self.df[self.df['word'].str[pos] != letter]

    def filter_grey(self, grey_letters: str):
        for letter in grey_letters:
            self.df = self.df[~self.df['word'].str.contains(letter)]

    def get_candidates(self):
        return self.df.reset_index(drop=True)
