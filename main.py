from stats import get_word_count
from stats import get_character_count
from stats import sort_size
from stats import print_letter_list
import sys
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return(file_contents)
def main():
    if len(sys.argv) ==2:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(filepath)
    wordcount= get_word_count(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    letters = get_character_count(text)
    letter_list = sort_size(letters)
    letter_list_print = print_letter_list(letter_list)
    print(letter_list_print)

main()