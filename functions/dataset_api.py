from functions.dataset import get_cleaned_data
from functions.input import input_capitalization

def get_column_names ():
    '''Returns the column names of the dataset.'''

    cleaned_data = get_cleaned_data()

    return cleaned_data[0]


def get_data_by_header_list(headers: 'list'):
    '''Retrieves all data within the columns listed inside the input list,
       
       arg: list of column names (ex. ['Year', 'Day']),
       
       returns a list of data based on the inputed headers.'''

    header_indexes = header_title_to_header_index(headers)

    data_based_on_headers = []

    for header_index in header_indexes:
        data_by_index = get_data_by_column_index(header_index)

        data_based_on_headers.append(data_by_index)
    
    merged_data = merge_list_data(data_based_on_headers)

    return merged_data


def merge_list_data(data: list[list]):
    '''Merges the contents of a list of lists by index,
    
       ex. [['YEAR', '2018'], ['DAY', '23']] => [['YEAR', 'DAY'], ['2018', '23']],
       
       arg: a list of column data as individual lists,

       returns a list of lists based on the format of the dataset.'''
    merged_list = []
    index_counter = 0
    
    while index_counter < len(data[0]):
        comb_row = []

        for element in data:
            comb_row.append(element[index_counter])

        merged_list.append(comb_row)
        index_counter += 1

    return merged_list


def header_title_to_header_index(headers: list):
    '''Matches the header title (of type string within a list) 
       to the appropriate header index of the dataset,
       
       ex. ['Year', 'Day'] => [3, 5],

       arg: a list containing header titles of type string,
       
       returns a list of the header indexes as integers.'''
    header_indexes = []

    column_names = get_column_names()

    for element in headers:
        header = input_capitalization(element)

        for index, element in enumerate(column_names):
            if header == element:
                header_indexes.append(index)
    
    return header_indexes


def get_data_by_column_index(index: int, start: int = 1, end: int = 0):
    '''Extracts all data of the indexed column and returns them as a list,
    
       ex. index = 3 => returning all data of column 'YEAR' as a list,

       args: column index as an integer, 
             starting row as an integer (default: first row, starting index: 1),
             final row as an integer (default: last row)
       
       returns the data inside the indexed column as a list.'''
    
    cleaned_data = get_cleaned_data()

    column_data = []

    if end == 0:
        # deliberately exclude last row from looping since it is empty
        end = len(cleaned_data)

    for row in range(start - 1, end):
        column_data.append(cleaned_data[row][index])

    return column_data