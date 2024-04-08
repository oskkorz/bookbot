book_path = "books/frankenstein.txt" 

def main():
    #book_path = "books/frankenstein.txt"
    text = read_function(book_path)
    #count_words = len(text.split())
    num_words = count_words(text)
    letters_count = char_occurences(text)

    print (f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")

    letters_list = []
    for char in letters_count:
        letters_list.append((char, letters_count[char]))
    letters_list.sort(reverse=True, key=sort_on)
    
    for char, count in letters_list:
        print (f"The '{char}' char was found: {count} times")

    print("--- End report ---")

   

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
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1

            else:
                char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict[1]


main()

