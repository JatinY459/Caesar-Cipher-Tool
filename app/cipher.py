import string
#constant values
LAST_LETTER_CODE = 90 #last letter code for 'Z'
FIRST_LETTER_CODE = 65 #first letter code for 'A'
ALPHABET_RANGE = 26 

def shift_char(char, shift):
    if char.isalpha():
        shifted = ord(char) + shift
        if(shifted > LAST_LETTER_CODE):
            # Coming back to start of alphabet when Z  gone ahead basically we circle back to A
            shifted -= ALPHABET_RANGE
        elif(shifted < FIRST_LETTER_CODE):
            # Coming back to end of alphabet when A is gone back basically we circle back to Z
            shifted += ALPHABET_RANGE
        return chr(shifted)
    return char


def caesar_shift(text, shift):
    # Take input text/message and shift value
    result = [] # Result string
    # loop through character but operating only on uppercase letters
    # Ignoring all other characters & adding them to result as is
    for char in text.upper():
        result.append(shift_char(char, shift))
    
    return "".join(result)


def caesar_decrypt_brute(text):
    results = []
    # Loop through all possible shifts i.e., 25 possible shift values
    for shift in range(1, ALPHABET_RANGE):
        # un-"caesar shifting" the text by shifting back by same number
        possible_message = caesar_shift(text, -shift)
        results.append(possible_message)
        # results.reverse() # Shift would be same as index+1 here
    return results


def caesar_decrypt_auto(text):
    # Get all possible decrypted messages of which one should be correct
    results = caesar_decrypt_brute(text)

    with open("app/common-words.txt", "r") as file:
        # Convert file into set
        common_words = set(word.strip().lower() for word in file)
    
    # Filter words in text
    words_in_text = text.lower().split()
    words_in_text = [word.strip(string.punctuation) for word in words_in_text]

    # Checking if all words in text are common English words or not
    for possible_message in results:
        # Filtering words in possible message
        possible_words = possible_message.lower().split()
        possible_words = [word.strip(string.punctuation) for word in possible_words]
        
        # all() function returns True if all elements are True
        # returns value (true or false) of "word" in common_words for all "word" in possible_words.
        has_valid_words = all(word in common_words for word in possible_words)
        if has_valid_words:
            return possible_message
        return False # If no valid words found, return False




# print(caesar_decrypt_auto("ifmmp"))