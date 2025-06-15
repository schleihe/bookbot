from stats import get_word_count
from stats import get_char_count 
from stats import get_sorted_char_list
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    args=sys.argv
    if(len(args)!=2):
        print("Invallid arguments")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath=args[1]
    print(f"{bookpath}")
    text=get_book_text(bookpath)
    num_words=get_word_count(text)
    char_set=get_char_count(text)
    sorted=get_sorted_char_list(char_set)
    #print(f"{num_words} words found in the document")
    #print(f"{char_set}")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")
    #print(get_book_text("books/frankenstein.txt"))

main()