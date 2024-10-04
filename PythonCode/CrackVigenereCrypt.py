import itertools

from CheckTheLanguageOfThePhrase import CheckTheLanguageOfThePhrase
from VigenereCrypt import VigenereDecrypt

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def loops_inside_loops(l, quantity_loops):
    yield from itertools.product(l, repeat=quantity_loops)


def brute_force_decrypt(phrase: str) -> str:
    phrase_decrypted = ""
    found = False

    alphabet_in_list = list(ALPHABET)
    for product_key in loops_inside_loops(alphabet_in_list, 3):

        unique_key = ''.join(product_key)
        product_phrase: str = VigenereDecrypt(phrase, unique_key)

        checker = CheckTheLanguageOfThePhrase()
        checker.break_the_phrase(product_phrase)
        result_analysis = checker.return_the_language()
        if result_analysis.found:
            phrase_decrypted = product_phrase
            break

    return phrase_decrypted
