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

# Пример использования:
finder = UniqueLetterFinder("""
The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it. 
-- Geoffrey James, "The Tao of Programming"
""")
print(finder.find_unique_letters())
print(finder.find_first_unique_letter())
