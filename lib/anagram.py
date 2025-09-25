class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list_of_words):
        sorted_word = sorted(self.word)
        return [word for word in list_of_words if sorted(word) == sorted_word]
