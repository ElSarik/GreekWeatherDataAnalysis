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


def get_data_by_column_index(index: int):
    '''Extracts all data of the indexed column and returns them as a list,
    
       ex. index = 3 => returning all data of column 'YEAR' as a list,

       arg: column index as an integer,
       
       returns the data inside the indexed column as a list.'''
    
    cleaned_data = get_cleaned_data()

    column_data = []

    for row in range(len(cleaned_data)):
        column_data.append(cleaned_data[row][index])

    return column_data


def get_highest_lowest_year(year_boundary: str = 'MAX'):
    '''Finds the maximum or the minimum available year in the dataset and returns that year,
    
       arg: string of value either 'MAX' or 'MIN',
       
       returns either the minimum or the maximum year.'''

    header_list = ['YEAR']
    data = get_data_by_header_list(header_list)

    data.sort()

    if year_boundary == 'MIN':
        return data[0]
    else:
        return data[-2]


# Task5 solution ~ @konspapp
def get_highest_temperature_by_year(year_min: int = 2006, year_max: int = 2018):
    '''Calculates and prints the highest temperature of every year,
    
       no-arg (default): Calculates between the lowest and the highest available year,
       arg1 (optional): lower boundary year as integer,
       arg2 (optional): upper boundary year as integer,
       
       prints the highest recorded temperature for each year.'''

    header_list = ['YEAR', 'HIGH_TEMP']
    data = get_data_by_header_list(header_list)

    highest_temp = 0

    for year in range(year_min, year_max + 1):
        for row in range(1, len(data)):
            temperature = data[row][1]

            try:
                temperature = float(temperature)
            except:
                continue

            if data[row][0] == str(year):
                if temperature > highest_temp:
                    highest_temp = temperature

                highest_temp_of_year = highest_temp

        highest_temp = 0
        print('The highest temperature recorded in ' + str(year) + ' had a value of ' + str(highest_temp_of_year))


# Task6 solution ~ @konspapp
def get_highest_amount_of_rain():
    '''Calculates and displays the region with the highest amount of rain.'''

    header_list = ['STATION_REGION', 'STATION_NAME', 'YEAR', 'MONTH', 'DAY', 'RAIN']
    data = get_data_by_header_list(header_list)

    max_rain = 0

    for row in range(1, len(data)):
        rain = data[row][5]

        try:
            rain = float(rain)

        except:
            continue

        if rain > max_rain:
            max_rain = rain
            result = [data[row][0], data[row][1], data[row][2], data[row][3], data[row][4], data[row][5], ]

    print(result)