class UniqueLetterFinder:
    def __init__(self, text):
        self.text = text

    def find_unique_letters(self):
        words = self.text.split()
        unique_letters = []

        for word in words:
            for letter in word:
                if word.count(letter) == 1:
                    unique_letters.append(letter)
                    break

        return unique_letters

    def find_first_unique_letter(self):
        unique_letters = self.find_unique_letters()

        for letter in unique_letters:
            if unique_letters.count(letter) == 1:
                return letter

        return None
