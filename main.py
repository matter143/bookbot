from stats import count_words, to_char


def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = count_words(file_contents)
    # print(f"{num_words} words found in the document")
    num_char = to_char(file_contents)
    print(num_char)


main()
