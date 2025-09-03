import sys

from stats import count_words, count_chars, sort_dict

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    words = get_book_text(sys.argv[1])
    chars = count_chars(words)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(words)} total words")
    print("--------- Character Count -------")
    for char in sort_dict(chars):
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    
if __name__ == "__main__":
    main()