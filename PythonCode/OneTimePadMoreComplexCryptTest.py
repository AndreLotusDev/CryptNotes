import unittest

from OneTimePadMoreComplexCrypt import digest_a_phrase


class OneTimePadMoreComplexCryptTest(unittest.TestCase):
    def test_if_go_and_back_return_the_same_phrase(self):
        phrase_to_use = "lorem ipsum test lorem ipsum"
        key =           "key as the same size of lore"

        phrase_digested = digest_a_phrase(phrase_to_use, key)
        phrase_decrypted_again = digest_a_phrase(phrase_digested, key)

        self.assertEqual(phrase_to_use, phrase_decrypted_again)