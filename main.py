from stats import count_words


def get_book_text(path):
    with open(path) as f:
        file_content = f.read()

    return file_content


def main():
    file_content = get_book_text("./books/frankenstein.txt")
    number_of_words = count_words(file_content)
    print(f"{number_of_words} words found in the document")

if __name__ == "__main__":
    main()
