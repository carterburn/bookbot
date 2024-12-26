def count_words(contents: str):
    return len(contents.split())

def count_chars(contents):
    counts = {}
    for c in contents:
        if c.lower() in counts:
            counts[c.lower()] += 1
        else:
            counts[c.lower()] = 1

    return counts

def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")

    print(f"{words} words found in the document\n")

    char_list = []
    for (k,v) in chars.items():
        if k.isalpha():
            char_list.append((k, v))

    char_list.sort(reverse=True, key=lambda x: x[1])

    for (char, amt) in char_list:
        print(f"The '{char}' character was found {amt} times")

    print("--- End report ---")

def read_file(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = 'books/frankenstein.txt'
    file_contents = read_file(book_path)

    words = count_words(file_contents)
    chars = count_chars(file_contents)

    print_report(book_path, words, chars)

main()
