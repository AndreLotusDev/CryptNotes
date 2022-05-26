class Helper:

    @staticmethod
    def clean_other_symbols(text_to_clean: str, list_to_check: list[str]) -> str:
        new_char_to_return: str = ''

        for char in text_to_clean:

            if char.upper() in list_to_check:
                new_char_to_return += char

        return new_char_to_return
