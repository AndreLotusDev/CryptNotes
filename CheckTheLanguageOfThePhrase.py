import io
from collections import namedtuple


class CheckTheLanguageOfThePhrase:
    __LANGUAGE_PT_BR = "PT-BR"
    __LANGUAGE_EN_US = "EN-US"
    __NONE_LANGUAGE = ""

    __LANGUAGE_PT_BR_TEXT: str = "dic_pt_br.txt"
    __LANGUAGE_EN_US_TEXT: str = "dic_en_us.txt"

    __ONE_MORE_WORD_FOUND: int = 1

    __count_in_portuguese: int = 0
    __count_in_english: int = 0

    __dic_in_portuguese: list[str] = []
    __dic_in_english: list[str] = []

    __total_words_in_phrase: int = 0
    __acceptable_tolerance: int = 50

    def __init__(self):
        words_in_portuguese = io.open(self.__LANGUAGE_PT_BR_TEXT, "r")
        self.__dic_in_portuguese = words_in_portuguese.read().split("/n")

        words_in_english = io.open(self.__LANGUAGE_EN_US_TEXT, "r")
        self.__dic_in_english = words_in_portuguese.read().split("/n")

        words_in_portuguese.close()
        words_in_english.close()

    def break_the_phrase(self, phrase_to_check: str) -> list:

        word_separate: list[str] = phrase_to_check.split(" ")
        self.__total_words_in_phrase = word_separate.count()

        for word in word_separate:
            word_found_in_some_language = self.__check_if_word_exist_in_one_dictionary(word)
            self.__check_if_word_exist_in_one_dictionary(word_found_in_some_language)

    def __check_if_word_exist_in_one_dictionary(self, word: str) -> str:

        word = word.upper()

        if word in self.__dic_in_portuguese:
            self.__add_score(self.__LANGUAGE_PT_BR)
            return self.__LANGUAGE_PT_BR
        elif word in self.__dic_in_english:
            self.__add_score(self.__LANGUAGE_EN_US)
            return self.__LANGUAGE_EN_US
        else:
            return self.__NONE_LANGUAGE

    def __add_score(self, language_found: str) -> None:
        if self.__LANGUAGE_PT_BR == language_found:
            self.COUNT_IN_PORTUGUESE += self.__ONE_MORE_WORD_FOUND
        elif self.__LANGUAGE_EN_US == language_found:
            self.COUNT_IN_ENGLISH += self.__ONE_MORE_WORD_FOUND

    @staticmethod
    def __calc_percentage(quantity_found, total_words) -> int:
        percentage = 100 * float(quantity_found)/float(total_words)
        return int(percentage)

    def return_the_language(self) -> tuple:
        language_info = namedtuple("found", "type_language")

        if self.__calc_percentage(self.__count_in_portuguese, self.__total_words_in_phrase) \
                > self.__acceptable_tolerance:
            return language_info(True, "PT-BR")

        elif self.__calc_percentage(self.__count_in_english, self.__total_words_in_phrase) \
                > self.__acceptable_tolerance:
            return language_info(True, "EN-US")
