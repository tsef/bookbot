from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()

    return file_content


def main():
    pretty_print_stats(sys.argv[1])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()
