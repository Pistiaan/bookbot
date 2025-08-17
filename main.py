from stats import count_words, count_letters, book_report

def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content

def print_report(filepath, content_string, dict_list):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}...')
    print('----------- Word Count ----------')
    count_words(content_string)
    print('--------- Character Count -------')
    for entry in dict_list:
        print(f'{entry["char"]}: {entry["num"]}')
    print('============= END ===============')

def main(filepath):
    content_string = get_book_text(filepath)
    letter_dict = count_letters(content_string)
    dict_list = book_report(letter_dict)
    print_report(filepath, content_string, dict_list)

main('books/frankenstein.txt')