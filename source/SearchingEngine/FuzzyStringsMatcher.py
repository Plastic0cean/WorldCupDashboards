#TODO: Reduce coupling by injecting SequenceMatcher into FuzzyStringMatcher
from difflib import SequenceMatcher 

def tokenize_text(text: str) -> list[str]:
    return text.split(" ")


class FuzzyStringsMatcher:

    def __init__(self, ratio: float, ignore_cases: bool=True) -> None:
        self.ratio = ratio
        self.ignore_cases = ignore_cases

    def calculate_similarity(self, string: str, second_string: str) -> float:
        if self.ignore_cases:
            string = string.lower()
            second_string = second_string.lower()
        return SequenceMatcher(a=string, b=second_string).ratio()
    
    def are_similar(self, string: str, second_string: str) -> bool:
        return self.calculate_similarity(string, second_string) >= self.ratio
    
    def contains_word(self, text: str, searched_word: str) -> bool:
        words = tokenize_text(text) 
        for word in words:
            if self.are_similar(searched_word, word):
                return True
        return False
    
    def contains_substring(self, text: str, substring: str) -> bool:
        text_len = len(text)
        substring_len = len(substring)
        for i in range(text_len-substring_len+1):
            if self.are_similar(text[i:i+len(substring)], substring):
                return True
        return False