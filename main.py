from stats import get_num_words, char_count, build_sorted_char_list 
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)




def main():
    book_path = sys.argv[1] 
    text = get_book_txt(book_path)
    num_words = get_num_words(text)
    chars = char_count(text)
    sorted_items = build_sorted_char_list(chars)
    print("========= BOOKBOT =========")
    print(f"Analyzing book found at {book_path}...")
    print("--------- Word Count ---------")
    print(f"Found {num_words} total words")
    print("------- Character Count -------")
    for item in sorted_items:
          ch = item["char"]
          if ch.isalpha():
               print(f"{ch}: {item['num']}")
    print("========= END =========")


def get_book_txt(path):
    with open(path) as f:
        return f.read()

main()


