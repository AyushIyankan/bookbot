def generate_report(book_path, hashMap, words_length):
    report = f"""--- Begin report of {book_path} ---\n{
        words_length} words found in the document\n\n"""

    for entry in hashMap:
        if str(entry).isalpha():
            report += f"""The '{entry}' character was found {
                hashMap[entry]} times\n"""

    print(report)


def count_characters(text):
    hashMap = {}

    for char in text:
        if char in hashMap:
            hashMap[char] += 1
        else:
            hashMap[char] = 1

    return hashMap


def count_words(text):
    words = text.split()
    return len(words)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_file_contents = file_contents.lower()
        hashMap = count_characters(lower_file_contents)
        words_length = count_words(lower_file_contents)
        generate_report("books/frankenstein.txt", hashMap, words_length)


if __name__ == "__main__":
    main()
