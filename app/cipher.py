#constant values
LAST_LETTER_CODE = 90 #last letter code for 'Z'
ALPHABET_RANGE = 26 # 26 letters in the alphabet

def caesar_shift(text, shift):
    # Take input text/message and shift value
    # Result string
    result = []
    # loop through character but operating only on uppercase letters
    # Ignoring all other characters & adding them to result as is
    for char in text.upper():
        if char.isalpha():
            shifted = ord(char) + shift
            if shifted > LAST_LETTER_CODE:
                # Coming back to start of alphabet when Z  gone ahead basically we circle back to A
                shifted -= ALPHABET_RANGE
            result.append(chr(shifted))
        else:
            result.append(char)
    return result


def caesar_decrypt_brute(text):
    results = []
    # Loop through all possible shifts i.e., 25 possible shift values
    for shift in range(1, ALPHABET_RANGE):
        # un-"caesar shifting" the text by shifting back by same number
        possible_message = caesar_shift(text, -shift)
        results.append(possible_message)
    return results


