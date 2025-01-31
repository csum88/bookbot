def word_count(book):
    words = book.split()
    return len(words)

def character_count(book):
    book_chars = list(book.lower())
    char_dict = {}
    for char in book_chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    #print(char_dict)
    return char_dict

def sort_alphabet(book):
    return book["num"]


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)
        #print(f"This book contains {word_count(file_contents)} words")
        #print(f"The following is a count of each individual character occurence in this book: {character_count(file_contents)}")

    sorted_list = [{'char':char, 'num':num} for char, num in character_count(file_contents).items() if char.isalpha()]
    sorted_list.sort(reverse=True, key=sort_alphabet)
    for sorted in sorted_list:
        print(f"The '{sorted['char']}' character was found {sorted['num']} times ")
    

   
    


main()

