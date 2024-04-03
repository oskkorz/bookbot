def main():
    book_path = "books/frankenstein.txt"
    text = read_function(book_path)
    #count_words = len(text.split())
    num_words = count_words(text)
    letters_count = char_occurences(text)
    print(num_words, letters_count)

def read_function(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def char_occurences(text):
    char_count = {}
    low = text.lower()
    #return len(low)
    for char in low:
        if char in char_count:
            char_count[char] += 1

        else:
            char_count[char] = 1

    return char_count



main()

