# Code to analyze a random text inputed by the user 

def count_word(text):
    return len(text.split())


def count_character(text): 
    return len(text.replace(" ",""))

def most_frequent_word(text):
    words = text.lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    max_count = max(word_count.values())

    result = []
    for word, count in word_count.items():
        if count == max_count:
            result.append(word)

    return result


def search_word(text, word): 
    return word.lower() in text.lower()

def reverse_text(text): 
    return text[::-1]


# Usage example 
if __name__ == "__main__": 
    text = input("Enter a text: ")
    print(f"word count: {count_word(text)}")
    print(f"count character: {count_character(text)}")
    print(f"The most frequent word is: {most_frequent_word(text)}")
    
    word = input("enter a word: ")
    print(f"Found? {search_word(text,word)}")

    print(f"The reverse of the text is: {reverse_text(text)}")

