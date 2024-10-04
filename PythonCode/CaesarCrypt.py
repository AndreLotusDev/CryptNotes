ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 3


def caesar_encrypt(plain_text: str) -> str:
    cipher_text: str = ''
    plain_text = plain_text.upper()

    for char in plain_text:
        index_in_alphabet: int = ALPHABET.find(char)

        # will return a module, with an offset
        index: int = (index_in_alphabet + KEY) % len(ALPHABET)

        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text


def caesar_decrypt(cipher_text: str) -> str:
    plain_text: str = ''

    for char in cipher_text:
        index_in_alphabet: int = ALPHABET.find(char)

        # will return a module, with an offset
        index: int = (index_in_alphabet - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

    return plain_text


def caesar_decrypt(cipher_text: str, key: int) -> str:
    plain_text: str = ''

    for char in cipher_text:
        index_in_alphabet: int = ALPHABET.find(char) + 1
        sum_between_actual_index_more_key = index_in_alphabet + key

        if sum_between_actual_index_more_key > len(ALPHABET):
            key_to_use_in_decrypt = sum_between_actual_index_more_key - (len(ALPHABET) + 1)
            plain_text += ALPHABET[key_to_use_in_decrypt]

        else:
            plain_text += ALPHABET[sum_between_actual_index_more_key - 1]

    return plain_text
