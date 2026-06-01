from merchant_galaxy.parser import Parser
from merchant_galaxy.utility import read_from_file
from merchant_galaxy.user_input import select_folder, get_alien_value, get_metal_value, get_questions_conversion


def main():
    """Run the application."""
    while True:
        selection = select_folder()
        if selection == "manual":
            alien_value = get_alien_value()
            metal_values = get_metal_value()
            questions_credit, question_value = get_questions_conversion()
            parser = Parser(alien_value, metal_values, question_value, questions_credit)
            parser.answer_question()
        elif selection == "file":
            list_value = read_from_file("input.txt")
            parser = Parser(list_value["alien_definition"], list_value["metal_definition"], list_value["question_value"], list_value["question_credit"])
            parser.answer_question()
        elif selection == "exit":
            print("Goodbye!")
            break




if __name__ == '__main__':
    main()
















