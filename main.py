import sys
from stats import get_num_words, get_char_count, sort_char_counts

def main():

    # Prints error message if user gives incorrect input
    if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

    # Gives filepath and initial print statement
    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    # Creates variable of the rest in the file
    text = get_book_text(filepath)
    
    # Prints the word count
    wordcount = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    
    char_counts = get_char_count(text)
    sorted_chars = sort_char_counts(char_counts)
    
    # Prints the character count
    print("--------- Character Count -------")
    for item in sorted_chars:
        #omits characters that are NOT letters
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

# Reads contents of and returns contents as a string
def get_book_text(filepath):

    with open(filepath, 'r') as f:

        file_contents = f.read()
    return file_contents





main()



