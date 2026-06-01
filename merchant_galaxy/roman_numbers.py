class RomanNumbers:
    VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    @staticmethod
    def sanitize_input(s: str) -> None:

        """Validate a Roman numeral.

        Checks that:

        - Only valid Roman numeral characters are used.

        - Invalid repetitions are not present.

        - Only valid subtractive notation pairs are used.

        Args:

            s: Roman numeral string to validate.

        Raises:

            ValueError: If the numeral contains invalid characters.

            ValueError: If the numeral contains invalid repetitions.

            ValueError: If the numeral contains invalid subtractive notation.

        """

        for char in s:

            if char not in RomanNumbers.VALUES:
                raise ValueError(f"Invalid Roman numeral character: {char}")

        invalid_repetitions = {

            "VV",

            "LL",

            "DD",

            "IIII",

            "XXXX",

            "CCCC",

            "MMMM",

        }

        for sequence in invalid_repetitions:

            if sequence in s:
                raise ValueError(

                    f"Invalid repetition found in Roman numeral: {sequence}"

                )

        valid_subtractive_pairs = {

            "IV",

            "IX",

            "XL",

            "XC",

            "CD",

            "CM",

        }

        for i in range(len(s) - 1):

            current = RomanNumbers.VALUES[s[i]]

            next_value = RomanNumbers.VALUES[s[i + 1]]

            if current < next_value:

                pair = s[i:i + 2]

                if pair not in valid_subtractive_pairs:
                    raise ValueError(

                        f"Invalid subtractive notation: {pair}"

                    )


    @staticmethod

    def roman_to_int(s: str) -> int:

        """Convert a Roman numeral to an integer.

        Args:

            s: Roman numeral string.

        Returns:

            The integer representation of the Roman numeral.

        Raises:

            ValueError: If the Roman numeral is invalid.

        """

        RomanNumbers.sanitize_input(s)

        total = 0

        previous_value = 0

        for char in s:

            current_value = RomanNumbers.VALUES[char]

            if current_value > previous_value:

                total += current_value - (2 * previous_value)

            else:

                total += current_value

            previous_value = current_value

        return total