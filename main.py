from stats import get_num_words, char_count 

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_txt(book_path)
    num_words = get_num_words(text)
    chars = char_count(text)
    print(f"Found {num_words} total words")
    print(f"Found {chars} total characters")


def get_book_txt(path):
    with open(path) as f:
        return f.read()

main()


