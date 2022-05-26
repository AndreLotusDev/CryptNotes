from Helper import Helper

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET_WITH_SPACE = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def VigenereCrypt(phrase: str, key: str) -> str:
    phrase = phrase.upper()
    phrase_cleaned = Helper.clean_other_symbols(phrase, ALPHABET_WITH_SPACE)

    key = key.upper()
    key_index: int = 0

    new_phrase_encrypted: str = ""

    for char in phrase_cleaned:

        if char == " ":
            new_phrase_encrypted += " "
            continue

        index = (ALPHABET.find(char) + ALPHABET.find(key[key_index])) % len(ALPHABET)
        new_phrase_encrypted += ALPHABET[index]

        key_index += 1

        should_reset_index = key_index == len(key)
        if should_reset_index:
            key_index = 0

    return new_phrase_encrypted


def VigenereDecrypt(phrase: str, key: str) -> str:
    phrase = phrase.upper()
    phrase_cleaned = Helper.clean_other_symbols(phrase, ALPHABET_WITH_SPACE)

    key = key.upper()
    key_index: int = 0

    new_phrase_decrypted: str = ""

    for char in phrase_cleaned:

        if char == " ":
            new_phrase_decrypted += " "
            continue

        index = (ALPHABET.find(char) - ALPHABET.find(key[key_index])) % len(ALPHABET)
        new_phrase_decrypted += ALPHABET[index]

        key_index += 1

        should_reset_index = key_index == len(key)
        if should_reset_index:
            key_index = 0

    return new_phrase_decrypted
