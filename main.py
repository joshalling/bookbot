import sys
from stats import get_num_words

paths = sys.argv[1:]
alphabet = "abcdefghijklmnopqrstuvwxyz"


def print_report(path, word_count, character_count):
    sorted_character_count = sorted(
        character_count.items(), key=lambda item: item[1], reverse=True
    )

    print(f"--- Report for {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter, count in sorted_character_count:
        print(f"{letter}: {count}")


for path in paths:
    with open(path) as f:
        file_contents = f.read()

    word_count = get_num_words(file_contents)
    character_count = {}
    for letter in file_contents:
        letter = letter.lower()
        if letter in alphabet:
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1

    print_report(path, word_count, character_count)
