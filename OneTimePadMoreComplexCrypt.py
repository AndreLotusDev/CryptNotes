def __bitwise_char(char_to_shuffle: chr, shuffle_char: chr) -> chr:
    if len(char_to_shuffle) > 1:
        raise Exception("Should not be bigger than 1")

    if len(shuffle_char) > 1:
        raise Exception("Should not be bigger than 1")

    char_binary = ''.join(format(ord(i), '08b') for i in char_to_shuffle)
    shuffle_char_binary = ''.join(format(ord(i), '08b') for i in shuffle_char)

    shuffle_operation = int(char_binary, 2) ^ int(shuffle_char_binary, 2)  # brings an integer
    new_char_utf_8 = chr(shuffle_operation)

    return new_char_utf_8


def digest_a_phrase(phrase_to_shuffle: str, phrase_to_use_as_key: str) -> str:
    if len(phrase_to_shuffle) != len(phrase_to_use_as_key):
        raise Exception("The key is different len than the phrase to shuffle")

    new_phrase_to_delivery: str = ""

    for index, char in enumerate(phrase_to_shuffle):
        new_phrase_to_delivery += __bitwise_char(phrase_to_shuffle[index], phrase_to_use_as_key[index])

    return new_phrase_to_delivery