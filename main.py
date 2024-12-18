def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = convert_dict_to_list(chars_dict)
    
    #sort list by count in descending order
    chars_list.sort(reverse=True, key=lambda x: x["count"])

    #print report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


def convert_dict_to_list(chars_dict):
    char_list = []
    for char, count in chars_dict.items():
        if char.isalpha():
            chars_dict = {"char": char, "count": count}
            char_list.append(chars_dict)
    return char_list
main()
