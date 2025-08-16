from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def main(filepath):
    content_string = get_book_text(filepath)
    count_words(content_string)

main('books/frankenstein.txt')
