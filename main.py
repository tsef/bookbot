from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()

    return file_content


def main():
    pretty_print_stats("./books/frankenstein.txt")

if __name__ == "__main__":
    main()
