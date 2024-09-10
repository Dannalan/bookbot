def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) #prints the whole ass text
    word_count = get_word_count(text)
    how_many_letters = get_letter_count(text.lower()) #printing how many letters
    sorted_dict = sort_dict(how_many_letters) #whole directory sorted

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")

def get_book_text(path):    
    with open(path) as f:
        return f.read()

def get_word_count(text_to_be_counted):
    return len(text_to_be_counted.split())

def get_letter_count(letters_to_be_counted):
    letter_count = {}
    for letters in letters_to_be_counted:
        letter_count[letters]=letter_count.setdefault(letters, 0) + 1
    return letter_count

def sort_on(d):
    return d["num"] #this tells sort() where to sort, in this case, its the numbers

def sort_dict(dict_to_be_sorted):
    sorted_list = []
    for characters in dict_to_be_sorted:
        sorted_list.append({"char": characters, "num": dict_to_be_sorted[characters]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()