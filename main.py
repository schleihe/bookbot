from stats import get_word_count
from stats import get_char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    text=get_book_text("books/frankenstein.txt")
    num_words=get_word_count(text)
    char_set=get_char_count(text)
    print(f"{num_words} words found in the document")
    print(f"{char_set}")
    #print(get_book_text("books/frankenstein.txt"))

main()