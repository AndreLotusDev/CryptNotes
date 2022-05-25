from CaesarCrypt import caesar_encrypt
from CrackCaesarCrypt import crack_with_brute_force, caesar_crack_with_smart_analysis, clean_other_symbols
import unittest


class CrackCaesarCryptTest(unittest.TestCase):

    def test_brute_force_will_pick_a_valid_word(self):
        FOUND: bool = True
        found_a_valid_word: bool = False

        options_to_check: list = crack_with_brute_force('WHVW')

        for option in options_to_check:

            option: str = option
            if option.upper() == 'TEST':
                found_a_valid_word = True

        self.assertEqual(FOUND, found_a_valid_word)

    def test_smart_analysis_will_pick_a_valid_word(self):
        PHRASE_TO_CHECK = "Collections, be they linear or nonlinear, have a defined set of properties that describe " \
                          "them and operations that can be performed on them. An example of a collection property is " \
                          "the collections Count, which holds the number of items in the collection. Collection " \
                          "operations, called methods, include Add (for adding a new element to a collection), " \
                          "Insert (for adding a new element to a collection at a specified index), Remove (for " \
                          "removing a specified element from a collection), Clear (for removing all the elements from " \
                          "a collection), Contains (for determining if a specified element is a member of a " \
                          "collection), and IndexOf (for determining the index of a specified element in a " \
                          "collection). rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"

        phrase_to_check = clean_other_symbols(PHRASE_TO_CHECK)

        FOUND: bool = True
        found_a_valid_word: bool = False

        encrypted_message = caesar_encrypt(phrase_to_check)
        options_to_check: list = caesar_crack_with_smart_analysis(encrypted_message)

        for option in options_to_check:

            option: str = option
            if option.upper() == phrase_to_check.upper():
                found_a_valid_word = True

        self.assertEqual(FOUND, found_a_valid_word)
