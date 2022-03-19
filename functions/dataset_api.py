from operator import ge
from functions.dataset import get_cleaned_data
from functions.input import input_capitalization

def get_column_names ():
    '''Returns the column names of the dataset.'''

    cleaned_data = get_cleaned_data()

    return cleaned_data[0]


def get_data_by_header_list(headers: 'list', start: int = 1, end: int = 0):
    '''Retrieves all data within the columns listed inside the input list,
       
       arg: list of column names (ex. ['Year', 'Day']),
       
       returns a list of data based on the inputed headers.'''

    header_indexes = header_title_to_header_index(headers)

    data_based_on_headers = []

    for header_index in header_indexes:
        data_by_index = get_data_by_column_index(header_index, start, end)

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

       args: column index as integer, 
             starting row as integer (default: first row, starting index: 1),
             final row as integer (default: last row)
       
       returns the data inside the indexed column as a list.'''
    
    cleaned_data = get_cleaned_data()

    column_data = []

    if end == 0:
        # deliberately exclude last row from looping since it is empty
        end = len(cleaned_data)

    for row in range(start - 1, end):
        column_data.append(cleaned_data[row][index])

    return column_data



def get_data_by_row(index: int):
    '''Extracts all data of the indexed row and returns them as a list,
    
       ex. index = 3 => returning all data of row 3 as a list,

       arg: row index as an integer, 
       
       returns the data inside the indexed row as a list.'''

    cleaned_data = get_cleaned_data()

    row_data = cleaned_data[index]

    return row_data


def find_in_row_by_header(row: int, column_header: list):
    '''Retrieves the value which corresponds to the indexed row and column header,
    
       ex. row = 3,
           column_header = 'YEAR' => returns the value of column 'YEAR' in row 3,

       arg: row index as an integer, 
            column_header as a list

       returns the value corresponding to the indexed row and column header as a string.'''

    row_data = get_data_by_row(row)

    column_indices = header_title_to_header_index(column_header)

    for index in column_indices:
        row_header_value = row_data[index]
        return row_header_value

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

    print(f'{result[1]} station in {result[0]} had the highest amount of rain ({result[5]}) on {result[4]}/{result[3]}/{result[2]}')


#    -------------vandl's work-----------------------------------------------------------------------------#


#   creating a middle term function for later use.
def middleterm(arg):
    num_arg = []
    for i in arg:
        try:
            num_arg.append(float(i))
        except:
            continue
    return (sum(num_arg) / len(num_arg))


def five_highestorlowest_temperature_cities_in2018(arguement="none"):

    # Takes High, low , or none as argument and returns the 5 cities with lowest/highest temperature average in 2018

    cleaned_data = get_cleaned_data()

    arguement = arguement.lower()  # making argument case-insensitive

    #   filtering data

    data_in2018 = []
    # year_index = getindex("STATION NAME")

    for i in cleaned_data:
        #
        if i[3] == "2018":
            data_in2018.append(i)
        else:
            continue

    #   data_in2018 now has CSV rows only from year 2018
    #   headers NOT included in data_in2018!
    #   creating a list with all cities once

    cities = []
    for i in data_in2018:
        if i[2] not in cities:
            cities.append(i[2])

    high_temp_dictionary = {}
    low_temp_dictionary = {}

    for i in cities:
        low_temp_dictionary[i] = []

    for i in cities:
        high_temp_dictionary[i] = []
    #   {'Αγία Κυριακή Ιωαννίνων': [], 'Άρτα': []...

    for key in low_temp_dictionary:
        # creating variable as already existing key's value, appending in var the items we need and then putting var
        # back in key as value
        for row in data_in2018:
            if row[2] == key:
                var = low_temp_dictionary[key]  # this is the keys value!
                var.append(row[9])
                low_temp_dictionary[key] = var

    #   lowmiddleterm dictionary now has all low temperetures in a list as value for every key (city).

    #   finding middle term of each value and putting it as the new value in dictionary, using same logic as above.

    for key in low_temp_dictionary:
        var = low_temp_dictionary[key]
        low_temp_dictionary[key] = middleterm(var)

    # same for highest temps. 110- 133 are the only lines i could find a way not to duplicate...

    for key in high_temp_dictionary:
        # creating variable as already existing key's value, appending in var the items we need and then putting var
        # back in key as value
        for row in data_in2018:
            if row[2] == key:
                var = high_temp_dictionary[key]  # this is the keys value!
                var.append(row[7])
                high_temp_dictionary[key] = var

    # lowmiddleterm and highermiddleterm dictionaries now have all low temperetures in a list as value for every key (
    # city).

    #   finding middle term of each value and putting it as the new value in dictionary, using same logic as above.

    for key in high_temp_dictionary:
        var = high_temp_dictionary[key]
        high_temp_dictionary[key] = middleterm(var)

    lowest_temperature_cities2018 = []
    highest_temperature_cities2018 = []

    #   appending lowest and highest 5 temperature cities in list.
    for i in range(5):
        lowest_temperature_cities2018.append(min(low_temp_dictionary))
        low_temp_dictionary.pop(min(low_temp_dictionary))
        highest_temperature_cities2018.append(max(high_temp_dictionary))
        high_temp_dictionary.pop(max(high_temp_dictionary))

    #   returning data according to users arguement
    if arguement == "none":
        return "The cities with lowest temperatures in 2018 are:  " + ", ".join(
            lowest_temperature_cities2018) + "." + "\n" + "The cities with highest temperatures in 2018 are: " + ", ".join(
            highest_temperature_cities2018) + "."
    elif arguement == "low":
        return "The cities with lowest temperatures in 2018 are: " + ", ".join(lowest_temperature_cities2018) + "."
    elif arguement == "high":
        return "The cities with highest temperatures in 2018 are: " + ", ".join(highest_temperature_cities2018) + "."
    else:
        return "Invalid arguement. Valid arguements are High, Low or no arguement."


#   ----------------------------- task 4 ---------------------------------------

def middleterm_of_place_in_2006_and_2018(region):

    # Takes a greek region as arguement and compares the average temperature in 2018 with average temperature in
    # N-year, N based on which year has most data to compare.
    # e.g. middleterm_of_place_in_2006_and_2018('Θράκη)
    #  returns In Θράκη ,  2018 had excactly the same temperature as 2017

    cleaned_data = get_cleaned_data()
    regions = ['Ήπειρος', 'Θεσσαλία', 'Θράκη', 'Κρήτη', 'Μακεδονία', 'Ν. Αιγαίου', 'Ν. Ιονίου', 'Πελοπόννησος',
               'Στερεά Ελλάδα']

    n = 2006   # default n year

    if region not in regions:  # validation
        return "Arguement must be a greek region, case sensitive!"

    region_data_2018 = {}
    region_data_nyear = {}

    for i in cleaned_data:  # creating a dictionary with each regions city as key and empty list as value
        if i[1] == region and i[3] == '2018':
            region_data_2018[i[2]] = []

    year_and_data_lengths = {}  # finding what year has most data
    for i in range(2006, 2018):
        year_and_data_lengths[i] = []

    for year in range(2006, 2018):
        for row in cleaned_data:
            if row[1] == region and row[3] == str(year):
                var = year_and_data_lengths[year]
                if row[2] not in year_and_data_lengths[year]:  # in each year/key, each city must be only once
                    var.append(row[2])
                year_and_data_lengths[year] = var

    for key in year_and_data_lengths: # finding which year has most cities as value / most data
        year_and_data_lengths[key] = len(year_and_data_lengths[key])

    n = max(year_and_data_lengths)  # according to task, we compare 2018 to year with most data / with max
    # year_and_data_lengths

    for i in cleaned_data:
        if i[1] == region and i[3] == str(n):
            region_data_nyear[i[2]] = []

    # data in 2018
    data_in_2018 = []
    for i in cleaned_data:
        if i[3] == '2018':
            data_in_2018.append(i)

    data_in_nyear = []
    for i in cleaned_data:
        if i[3] == '2018':
            data_in_nyear.append(i)

    for key in region_data_2018:  # in region_data_2018 appending each MEAN_TEMP as value in list for each city in
        # region.
        for row in data_in_2018:
            if row[2] == key:
                var = region_data_2018[key]
                var.append(row[6])  # appending in value the mean temp
                region_data_2018[key] = var

    # for nyear
    for key in region_data_nyear:  # in region_data_2018 appending each MEAN_TEMP as value in list for each city
        # in region.
        for row in data_in_nyear:
            if row[2] == key:
                var = region_data_nyear[key]
                var.append(row[6])  # appending in value the mean temp
                region_data_nyear[key] = var

    for key in region_data_2018:  # value = middle term([MEANS_TEMPS])
        var = region_data_2018[key]
        region_data_2018[key] = middleterm(var)
    for key in region_data_nyear:
        var = region_data_nyear[key]
        try:  # there are some empty lists, try except because we will get zero division error in middle term function
            region_data_nyear[key] = middleterm(var)
        except:
            continue

    region_2018_tempslist = []
    region_nyear_tempslist = []

    for i in region_data_2018:
        region_2018_tempslist.append(region_data_2018[i])
    for i in region_data_nyear:
        region_nyear_tempslist.append(region_data_nyear[i])

    final_temperature_middle_term_2018 = round(middleterm(region_2018_tempslist), 2)  # middle term of temperatures
    # list, rounding to 2 decimals
    final_temperature_middle_term_nyear = round(middleterm(region_nyear_tempslist), 2)

    if final_temperature_middle_term_2018 > final_temperature_middle_term_nyear:
        return "In " + str(region) + ", 2018 was hotter than " + str(n) + " by " + str(
            round((final_temperature_middle_term_2018 - final_temperature_middle_term_nyear), 2)) + " degrees celcius."
    elif final_temperature_middle_term_2018 < final_temperature_middle_term_nyear:
        return "In " + str(region) + " , " + str(n) + " was hotter than 2018" + " by " + str(
            round((final_temperature_middle_term_nyear - final_temperature_middle_term_2018), 2)) + " degrees celcius."
    elif final_temperature_middle_term_2018 == final_temperature_middle_term_nyear:
        return "In " + str(region) + " , " + "2018 had excactly the same temperature as " + str(n)