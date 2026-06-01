from merchant_galaxy.utility import read_from_file
from merchant_galaxy.roman_numbers import RomanNumbers

class Parser:
    """Parses alien language definitions and answers user questions."""

    def __init__(self, alien_definitions: list, metal_definitions: list, questions_value: list, questions_credit: list):
        """Initialize the parser and load all data from the input file."""
        self.alien_definitions = alien_definitions
        self.metal_definitions = metal_definitions
        self.question_value = questions_value
        self.question_credit = questions_credit
        self.alien_value: dict = self._get_alien_to_roman_value()
        self.metal_value: dict = self._get_metal_value()
    def _get_alien_to_roman_value(self) -> dict[str, str]:
        """Build a mapping between alien words and Roman numerals.

                Returns:

                    A dictionary where the key is an alien word and the

                    value is its corresponding Roman numeral.

                """
        alien_dict = {}
        alien_words = self.alien_definitions
        for item in alien_words:
            splitter = item.split(" is ")
            if splitter[1] in RomanNumbers.VALUES.keys():
                alien_dict[splitter[0]] = splitter[1]
        return alien_dict

    def _get_metal_value(self) -> dict[str, float]:
        """Calculate the unit value of each metal.

                Returns:

                    A dictionary mapping metal names to their unit credit value.

                """
        dict_metal_credit: dict[str, float] = {}
        metal_words = self.metal_definitions
        for item in metal_words:
            splitter = item.split(" is ")

            second_splitter = splitter[0].split(" ")
            alien_series: list[str]= []
            metal_name: list[str] = []
            for element in second_splitter:
                if element[0].isupper():
                    metal_name.append(element)
                else:
                    alien_series.append(element)
            roman_string = "".join([self.alien_value[name] for name in alien_series])
            value_alien = RomanNumbers.roman_to_int(roman_string)
            third_splitter = splitter[1].split(" ")
            divider_value = int(third_splitter[0])
            dict_metal_credit[metal_name[0]] = divider_value / value_alien
        return dict_metal_credit

    def _alien_to_number(self, alien_sequence: list[str]) -> int:
        """Convert an alien numeral sequence into an integer.

                Args:

                    alien_sequence: List of alien words representing a number.

                Returns:

                    The integer value of the alien numeral sequence.

                """
        roman_string = "".join([self.alien_value[name] for name in alien_sequence])
        value_alien = RomanNumbers.roman_to_int(roman_string)
        return value_alien


    def answer_question(self) -> None:
        """Answer all questions found in the input file."""
        if self.question_value:
            for phrase in self.question_value:
                try:

                    temp= phrase.strip("?").split(" is ")

                    temp_1 = temp[1].strip().split(" ")

                    alien_sequence = temp_1
                    print(f"{' '.join(alien_sequence)} is {self._alien_to_number(alien_sequence)}")
                except (KeyError, IndexError):
                    print("I have no idea what are you talking about.")
        if self.question_credit:
            for phrase in self.question_credit:
                try:
                    temp= phrase.strip("?").split(" is ")

                    temp_1 = temp[1].strip().split(" ")

                    alien_sequence = []
                    metal_name = None
                    for element in temp_1:
                        if element.istitle():
                            metal_name = element
                        else:
                            alien_sequence.append(element)

                    print (f"{' '.join(alien_sequence)} {metal_name} is {self._alien_to_number(alien_sequence) * self.metal_value[metal_name]} Credits.")
                except (KeyError, IndexError):
                    print("I have no idea what are you talking about.")

