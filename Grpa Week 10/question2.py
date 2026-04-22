 class StringManipulation:
    def __init__(self, words: list):
        # Initialize the attribute with the given list of words
        self.words = words

    def total_words(self) -> int:
        # Return the total number of words
        return len(self.words)

    def count(self, some_word: str) -> int:
        # Return the number of times some_word appears in words
        return self.words.count(some_word)

    def words_of_length(self, length: int) -> list:
        # Return a list of words with the specified length
        return [word for word in self.words if len(word) == length]

    def words_start_with(self, char: str) -> list:
        # Return a list of words starting with the given character
        return [word for word in self.words if word.startswith(char)]

    def longest_word(self) -> str:
        # Return the longest word; if multiple, return the first occurrence
        if not self.words:
            return ""  # handle empty list case
        return max(self.words, key=len)

    def palindromes(self) -> list:
        # Return a list of words that are palindromes
        return [word for word in self.words if word == word[::-1]]
