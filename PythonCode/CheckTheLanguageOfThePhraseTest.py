import unittest

from CheckTheLanguageOfThePhrase import CheckTheLanguageOfThePhrase


class CheckTheLanguageOfThePhraseTest(unittest.TestCase):

    def test_if_will_understand_portuguese(self):

        IS_PORTUGUESE_LANGUAGE = True
        FORMAT_SHOULD_RETURN = "PT-BR"

        checker = CheckTheLanguageOfThePhrase()
        checker.break_the_phrase("Essa é uma frase em português, você consegue adivinhar")

        format_returned = checker.return_the_language()

        self.assertEqual(IS_PORTUGUESE_LANGUAGE, format_returned.found)
        self.assertEqual(FORMAT_SHOULD_RETURN, format_returned.type_language)

    def test_if_will_understand_english(self):
        IS_ENGLISH_LANGUAGE = True
        FORMAT_SHOULD_RETURN = "EN-US"

        checker = CheckTheLanguageOfThePhrase()
        checker.break_the_phrase("This is a phrase in english, could you tell")

        format_returned = checker.return_the_language()

        self.assertEqual(IS_ENGLISH_LANGUAGE, format_returned.found)
        self.assertEqual(FORMAT_SHOULD_RETURN, format_returned.type_language)

    def test_if_will_understand_that_is_not_a_valid_language(self):
        IS_INVALID_LANGUAGE = False

        checker = CheckTheLanguageOfThePhrase()
        checker.break_the_phrase("xx  xxxxxxxxxxxxxxxxx xxxxxxxxx fds sfg fg gh d h hdf dfgh dfgh dfgh hgfghfghfghfgh dfshosgfhugfhui fghjgfhj sdfgsgdfgdfgfdg")

        format_returned = checker.return_the_language()

        self.assertEqual(IS_INVALID_LANGUAGE, format_returned.found)