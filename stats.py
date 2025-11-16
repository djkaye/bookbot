def get_word_count(text):
    text_list = text.split()
    words = len(text_list)
    return(words)
def get_character_count(text):
    letters = {}
    letters_split = []
    booktext = list(text.lower())
    for letter in booktext:
        if letter in letters:
            quantity = letters[letter]
            new_quantity = quantity+1
            letters[letter] = new_quantity
        else:
            letters[letter] = 1   
    return(letters)

def sort_size(letter_list):
    sorted_list = []
    for letter in letter_list:
        mini_list = {}
        mini_list["letter"] = letter
        mini_list["num"] = letter_list[letter]
        sorted_list.append(mini_list)
    sorted_list.sort(reverse=True, key=sort_on)
    return(sorted_list)
def sort_on(items):
    return items["num"]
def print_letter_list(list):
    for mini_dict in list:
        letter = mini_dict["letter"]
        number = mini_dict["num"]
        print(f"{letter}: {number}")