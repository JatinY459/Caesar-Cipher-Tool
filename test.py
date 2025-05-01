# with open("app/common-words.txt", "r") as file:
#         common_words = set(word.strip() for word in file)

# print(list(common_words)[9])


# ----- #----- #----- #----- #----- #----- #----- #----- #----- #----- #----- #----- #----- #
import app.cipher as cipher

# print(cipher.caesar_decrypt_brute("ifmmp"))
# ----- #----- #----- #----- #----- #----- #----- #----- #----- #----- #----- #----- #----- #
LAST_LETTER_CODE = 90 #last letter code for 'Z'
ALPHABET_RANGE = 26
text = "ifmmp, xpsme!"
shift = -1
result = [] # Result string

print(cipher.caesar_decrypt_auto(text)) # works like a charm