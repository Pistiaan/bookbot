def count_words(book_string):
    word_count = len(book_string.split())
    print(f'{word_count} words found in the document')

def count_letters(book_string):
    letter_dict = {}
    lower_string = book_string.lower()
    for letter in lower_string:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else: letter_dict[letter] = 1
    print(letter_dict)