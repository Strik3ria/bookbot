def count_words(book):
    return len(book.split(' '))

def get_book_content(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def get_letter_count(book):
    count_dict = {}
    for letter in book.lower():
        if letter.isalpha():
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1

    count_dict = dict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))
    return count_dict



def main():
    path_to_file = "books/frankenstein.txt"
    book_content = get_book_content(path_to_file)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(book_content)} words found in document")
    print()

    letter_count = get_letter_count(book_content)

    for letter in letter_count.keys():
        print(f"The '{letter}' character was found {letter_count[letter]} times")

    print("--- End report ---")


if __name__ == '__main__':
    main()
