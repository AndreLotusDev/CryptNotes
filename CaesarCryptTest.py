from CaesarCrypt import caesar_encrypt, caesar_decrypt
import unittest

class CaesarCryptTest(unittest.TestCase):

    def test_if_cryting_is_giving_the_correct_word(self):

        message_cripted: str = caesar_encrypt('TEST')

        self.assertEqual(message_cripted, 'WHVW')

    def test_if_decrypting_is_giving_the_correct_word(self):

        message_cripted: str = caesar_decrypt('WHVW')

        self.assertEqual(message_cripted, 'TEST')