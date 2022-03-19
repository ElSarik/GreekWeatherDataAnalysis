import csv
import re
from pprint import pprint

global cleaned_data


def dataset_open():
    '''Opens the csv file,
    
       Returns csv content as a 2D list.'''

    # reading the file
    file = open('greek_weather_data.csv', encoding="utf8")
    csvreader = csv.reader(file)
    dataset = list(csvreader)

    return dataset


def dataset_split(dataset: 'list[list[str]]'):
    '''Splits the arg using '/t' as delimiter,

       arg: 2D str(list),
       
       Returns splitted 2D str(list).'''

    global cleaned_data

    data = []

    # breaking the list into elements
    for i in range(len(dataset)):
        i = [element for line in dataset[i] for element in line.split('\t')]
        data.append(i)

    cleaned_data = data

    return data

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

    global cleaned_data

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

    global cleaned_data
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
