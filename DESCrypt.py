from des import DesKey

ESPECIAL_CHAR = "$"


def add_padding(text_to_analyse: str, blocksize: int = 64) -> str:
    pad_len = blocksize - (len(text_to_analyse) % blocksize)

    padding_to_add = ESPECIAL_CHAR * pad_len
    return text_to_analyse + padding_to_add


def remove_add_padding(text_to_remove_padding: str) -> str:
    counter = 0

    for c in text_to_remove_padding[::-1]:
        if c == ESPECIAL_CHAR:
            counter += 1
        else:
            break  # doesn't make any sense to keep iterating throug the loop

    return text_to_remove_padding[:-counter]


def crypt(text_to_crypt: str, key: str) -> str:
    key_bin = DesKey(key.encode())
    crypted_bytes = key_bin.encrypt(text_to_crypt.encode(), padding=True)
    return crypted_bytes


def decrypt(text_to_decrypt: str, key_to_use: str) -> str:
    key_bin = DesKey(key_to_use.encode())
    decrypted_in_bytes = key_bin.decrypt(text_to_decrypt, padding=True)
    return decrypted_in_bytes.decode("utf-8")