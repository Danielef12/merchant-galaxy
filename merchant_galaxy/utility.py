def read_from_file(filename: str) -> dict[str, list[str]]:
    """Reads and categorizes lines from an input file.

    Categories:
        - question_credit: lines starting with "how many"
        - question_value: lines starting with "how much"
        - metal_definition: lines containing "Credits"
        - alien_definition: all remaining lines

    Args:
        filename: Path to the input file.

    Returns:
        A dictionary containing the categorized lines.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    question_credit: list[str] = []
    question_value: list[str] = []
    metal_definition: list[str] = []
    alien_definition: list[str] = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("how many"):
                question_credit.append(line)
            elif line.startswith("how much"):
                question_value.append(line)
            elif "Credits" in line:
                metal_definition.append(line)
            else:
                alien_definition.append(line)

    return {
        "question_credit": question_credit,
        "question_value": question_value,
        "metal_definition": metal_definition,
        "alien_definition": alien_definition,
    }