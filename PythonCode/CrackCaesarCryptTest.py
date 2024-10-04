from CaesarCrypt import caesar_encrypt
from CrackCaesarCrypt import crack_with_brute_force, caesar_crack_with_smart_analysis, clean_other_symbols, \
    caesar_crack_with_smart_analysis_and_machine_thinking
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
        PHRASE_TO_CHECK = "Tipos e eeeeeeeeeeeeeeeeeeeeeeeeeeeeee exemplos de frase Existem sete tipos principais de frases que utilizamos para nos comunicar. Depois de conhecer as definições, apresentaremos exemplos de cada uma delas. Você vai perceber que algumas frases se encaixam em mais de uma categoria."

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

    def test_smart_analysis_machine_thinking_will_pick_a_valid_word_pt(self):
        LANGUAGE_SHOULD_BE = "PT-BR"
        PHRASE_TO_CHECK = "Tipos e eeeeeeeeeeeeeeeeeeeeeeeeeeeeee exemplos de frase Existem sete tipos principais de frases que utilizamos para nos comunicar. Depois de conhecer as definições, apresentaremos exemplos de cada uma delas. Você vai perceber que algumas frases se encaixam em mais de uma categoria."

        phrase_to_check = clean_other_symbols(PHRASE_TO_CHECK)

        FOUND: bool = True
        found_a_valid_word: bool = False
        found_type_language: str = ""

        encrypted_message = caesar_encrypt(phrase_to_check)
        options_to_check: tuple = caesar_crack_with_smart_analysis_and_machine_thinking(encrypted_message)

        for option in options_to_check.list_of_possibilities:

            option: str = option
            if option.upper() == phrase_to_check.upper():
                found_a_valid_word = True
                found_type_language = options_to_check.type_language

        self.assertEqual(FOUND, found_a_valid_word)
        self.assertEqual(LANGUAGE_SHOULD_BE, found_type_language)

    def test_smart_analysis_machine_thinking_will_pick_a_valid_word_en_us(self):
        LANGUAGE_SHOULD_BE = "EN-US"
        PHRASE_TO_CHECK = "A phrase eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee is a group of two or more words that work together but don’t form a clause. In truth, “phrase” is a very broad term that we often use as a name for sayings, quotes, or other parts of every day speech, but this article will discuss phrases as they work in grammar."

        phrase_to_check = clean_other_symbols(PHRASE_TO_CHECK)

        FOUND: bool = True
        found_a_valid_word: bool = False
        found_type_language: str = ""

        encrypted_message = caesar_encrypt(phrase_to_check)
        options_to_check: tuple = caesar_crack_with_smart_analysis_and_machine_thinking(encrypted_message)

        for option in options_to_check.list_of_possibilities:

            option: str = option
            if option.upper() == phrase_to_check.upper():
                found_a_valid_word = True
                found_type_language = options_to_check.type_language

        self.assertEqual(FOUND, found_a_valid_word)
        self.assertEqual(LANGUAGE_SHOULD_BE, found_type_language)
