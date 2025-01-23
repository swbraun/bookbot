
def sort_on(dict):
    return dict["count"]

### end helper

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def print_report(filename, text):
    words = count_words(text)
    chars = count_characters(text)
    dict_list = []

    for char in chars:
        if char.isalpha():
            new_dict = {"letter": char, "count": chars[char]}
            dict_list.append(new_dict)
    dict_list.sort(key=sort_on, reverse=True)

    print(f"--- Begin report of {filename} ---")
    print(f"{words} words found in the document\n")

    for entry in dict_list:
        print(f"The '{entry['letter']}' character was found {entry['count']} times")

    print("--- End report ---")


def main():
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        file_contents = f.read()
    print_report(filename, file_contents)

main()

