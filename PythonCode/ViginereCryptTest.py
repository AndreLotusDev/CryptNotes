import unittest

from VigenereCrypt import VigenereCrypt, VigenereDecrypt


class ViginereCryptTest(unittest.TestCase):

    def test_if_crypt_will_bring_correct_encrypted_word(self):
        PHRASE_TO_CRYPT = "this phrase will be crypted"
        KEY = "ABCDEFG"
        SHOULD_RETURN_THIS_PHRASE_CRIPTED = "tikv tmxatg zmqr bf eucuzee".upper()

        phrase_crypted_to_check = VigenereCrypt(PHRASE_TO_CRYPT, KEY)

        self.assertEqual(SHOULD_RETURN_THIS_PHRASE_CRIPTED, phrase_crypted_to_check)

    def test_if_crypt_will_bring_correct_decrypted_word(self):
        PHRASE_TO_CRYPT = "this phrase will be crypted".upper()
        KEY = "ABCDEFG"

        phrase_to_decrypt_and_check = VigenereCrypt(PHRASE_TO_CRYPT, KEY)
        phrase_to_check_if_it_was_decrypted = VigenereDecrypt(phrase_to_decrypt_and_check, KEY)

        self.assertEqual(PHRASE_TO_CRYPT, phrase_to_check_if_it_was_decrypted)