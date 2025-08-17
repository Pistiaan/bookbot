def count_words(book_string):
    word_count = len(book_string.split())
    print(f'Found {word_count} total words')

def count_letters(book_string):
    letter_dict = {}
    lower_string = book_string.lower()
    for letter in lower_string:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else: letter_dict[letter] = 1
    return letter_dict

def sort_on(items):
    return items["num"]

def book_report(dict):
    dict_list = []
    for letter in dict:
        new_dict = {}
        if letter.isalpha():
            count = dict[letter]
            new_dict["char"] = letter
            new_dict["num"] = count
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list