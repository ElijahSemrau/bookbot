# Accepts text from book as a string and returns number of works in a string

def get_num_words(text):

    words = text.split()

    wordcount = len(words)

    return wordcount


# Accepts text from book as a string, converts all letters into lowercase, creates a dictionary and then fills dictionary with letters and counts
def get_char_count(text):

    lower_text = text.lower()
    char_counts = {}

    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


# Converts dictionary into multiple dictionaries with characters and number counts
def sort_char_counts(char_counts):

    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    def sort_on(item):
        return item["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list
