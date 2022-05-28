import unittest
from DESCrypt import crypt, decrypt

class DESCryptTest(unittest.TestCase):

    def test_if_go_and_back_return_the_same_phrase(self):
        phrase_to_use = "lorem ipsum test lorem ipsum"
        key = "key 8bit"

        phrase_crypted = crypt(phrase_to_use, key)
        phrase_uncrypted = decrypt(phrase_crypted, key)

        self.assertEqual(phrase_to_use.upper(), phrase_uncrypted.upper())