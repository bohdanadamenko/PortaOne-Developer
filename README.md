# Unique Letter Finder

This Python program finds the first unique character in each word of a given text, and then returns the first unique character from the set of these characters.

## Class: UniqueLetterFinder

The `UniqueLetterFinder` class takes a string of text as input and has two methods:

### Method: find_unique_letters

This method splits the text into words. For each word, it finds the first character that does not repeat in that word. These characters are added to a list, which is then returned.

### Method: find_first_unique_letter

This method first calls `find_unique_letters` to get a list of unique characters. It then iterates over this list and returns the first character that only appears once in the list. If no such character exists, it returns `None`.

## Example Usage

```python
finder = UniqueLetterFinder("The Tao gave birth to machine language. Machine language gave birth to the assembler.")
print(finder.find_unique_letters())
print(finder.find_first_unique_letter())
