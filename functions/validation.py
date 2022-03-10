from functions.dataset import get_cleaned_data
from functions.dataset_api import get_column_names
from functions.input import input_capitalization


def column_name_validation(input: str) -> bool:
    '''Checks if the input corresponds to a valid column name
       (case-sensitivity is not required)

       ex. input = 'Year' => True

       arg: input of type string,

       returns True if the input is a valid column name
           and False otherwise.'''

    columns = get_column_names()
    input = input_capitalization(input)

    if input in columns:
        return True
    else:
        return False


def column_index_validation(input: int) -> bool:
    '''Checks if the input corresponds to a valid column index

       ex. input = 23 => False

       arg: input of type integer (starting index: 0),

       returns True if the input is a valid column index
           and False otherwise.'''

    columns = get_column_names()
    index_range = len(columns) - 1

    if (input < 0 or input > index_range):
        return False
    else:
        return True


def row_index_validation(input: int) -> bool:
    '''Checks if the input corresponds to a valid row index

       ex. input = -4 => False

       arg: input of type integer (starting index: 0),

       returns True if the input is a valid row index
           and False otherwise.'''

    data = get_cleaned_data()
    index_range = len(data) - 1

    if (input < 0 or input > index_range):
        return False
    else:
        return True


def read_and_validate_index(validation_type: str) -> int:
    '''Reads and validates numeric inputs

      arg. validation_type: 'column_index', 'row_index'

      returns the first valid input given.'''

    while True:
        given_input = input()
        validation_function = validation_type + '_validation'

        try:
            given_input = int(given_input)
        except ValueError:
            print('Invalid input')
            continue
        else:
            successful_validation = eval(validation_function + '(given_input)')
            if successful_validation is True:
                break
            else:
                print('Invalid input')
                continue

    return given_input


def read_and_validate_name(validation_type: str) -> str:
    '''Reads and validates string inputs

       arg. validation_type: 'column_name'

       returns the first valid input given.'''

    while True:
        given_input = input()
        validation_function = validation_type + '_validation'

        successful_validation = eval(validation_function + '(given_input)')
        if successful_validation is True:
            break
        else:
            print('Invalid input')
            continue

    return given_input
