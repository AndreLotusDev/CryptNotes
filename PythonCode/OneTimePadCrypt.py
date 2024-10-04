import random

#DO NOT USE IN REAL SCENARIOS!

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SEED = "ABHJDSFBGHGBDFSDBGHgGKSFHJUIOFGSH"


def generate_random_key(char_to_cript: str) -> str:
    index_in_alphabet = ALPHABET.find(char_to_cript.upper())

    random.seed(SEED)

    magic_number = 0
    if index_in_alphabet > 0:
        magic_number = random.randint(0, index_in_alphabet)

    return ALPHABET[magic_number]


def encrypt(text_to_cript: str) -> str:
    new_phrase: str = ""
    text_to_cript = text_to_cript.upper()

    for char in text_to_cript:
        new_phrase += generate_random_key(char)

    return new_phrase


#ONLY FOR TEST PURPOUSE DOESNT MAKE SENSE
def decrypt(text_to_decrypt: str, key: str) -> str:
    new_phrase: str = ""
    key = key.upper()
    text_to_decrypt = text_to_decrypt.upper()

    for index, char in enumerate(text_to_decrypt):
        new_phrase += generate_random_key(key[index])

    return new_phrase