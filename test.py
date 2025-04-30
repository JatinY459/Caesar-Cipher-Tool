# with open("app/common-words.txt", "r") as file:
#         common_words = set(word.strip() for word in file)

# print(list(common_words)[9])

import app.cipher as cipher

print(cipher.caesar_decrypt_brute("ifmmp"))