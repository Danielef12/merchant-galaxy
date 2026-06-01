from merchant_galaxy.roman_numbers import RomanNumbers

def select_folder():
    """Select font of data"""
    while True:
        selection = input("Want to insert manual data or from file? (manual/file/exit): ")
        if selection in ["manual", "file", "exit"]:
            return selection
        else:
            print("Invalid selection")


def get_alien_value() -> list[str]:
    """Get alien values from manual input."""
    print("Insert alien values (e.g. 'glob is I').")
    print("Press Enter on an empty line to finish.")

    alien_values: list[str] = []

    while True:
        alien_input = input("Alien value: ").strip()

        if not alien_input:
            break
        if  len(alien_input.split(" ")) != 3:
            print("Invalid alien value")
        elif alien_input.split(" ")[2] not in RomanNumbers.VALUES:
            print("Invalid Roman value")
        else: alien_values.append(alien_input)

    return alien_values


def get_metal_value()-> list[str]:
    """Get metal values from manual input."""
    print("Insert metal values (e.g. 'glob glob Silver is 34 Credits').")
    print("Press Enter on an empty line to finish.")
    metal_values: list[str] = []
    while True:
        metal_input = input("Metal value: ").strip()
        if not metal_input:
            break
        if "is" not in metal_input:
            print("Invalid metal value")
            continue
        else:
            splitter = metal_input.split(" is ")
            parole = splitter[0].split(" ")
            parole[-1] = parole[-1].capitalize()
            splitter[0] = " ".join(parole)
            if splitter[1].lower().endswith("credits")  and splitter[1][0].isnumeric():
                splitter[1]= splitter[1].replace("credits", "Credits")
                metal_input= splitter[0] + " is " + splitter[1]
                metal_values.append(metal_input)
            else:
                print("Invalid metal value")
                continue
    return metal_values


def sanitize_questions(question) -> list[str]:
    """Sanitize questions from manual input."""
    if "is" in question:
        splitter = question.split(" is ")
        if not splitter[1].endswith("?"):
            splitter[1] += " ?"

        if splitter[0].endswith("credits"):
            splitter[0] = splitter[0].replace("credits", "Credits")

        if splitter[0].startswith("How many".lower()) and splitter[1].endswith("?"):
            second_split = splitter[1].split(" ")
            second_split[-2]= second_split[-2].capitalize()
            splitter[1] = " ".join(second_split)

    return splitter[0] + " is " + splitter[1]


def get_questions_conversion() -> tuple[list[str], list[str]]:
    """Get questions from manual input."""
    print("Insert questions (e.g. 'how many Credits is glob prok Silver ?').")
    print("Press Enter on an empty line to finish.")
    questions_credit: list[str] = []
    question_value: list[str] = []
    while True:
        question_input = input("Question: ").strip()
        if not question_input:
            break
        sanitized=sanitize_questions(question_input)

        if sanitized.startswith("how many"):
            questions_credit.append(sanitized)
        elif sanitized.startswith("how much"):
            question_value.append(sanitized)

    return questions_credit, question_value



