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
    # task #3. Να βρείτε τις 5 πόλεις/χωριά με τον υψηλότερο και χαμηλότερο μέσο όρο θερμοκρασιών για το 2018

    global cleaned_data

    arguement = arguement.lower()  # making arguement case insensitive

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

    #   headers NOT included in data_in2018!!!!!
    #   creating a list with all cities once
    cities = []
    for i in data_in2018:
        if i[2] not in cities:
            cities.append(i[2])

    high_temp_dictionary = {}
    low_temp_dictionary = {}

    # min temp == index 9
    # high temp == index 7

    for i in cities:
        low_temp_dictionary[i] = []

    for i in cities:
        high_temp_dictionary[i] = []
    #   {'Αγία Κυριακή Ιωαννίνων': [], 'Άρτα': []...

    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
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
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------
    #   finding middle term of each value and putting it as the new value in dictionary, using same logic as above.

    for key in high_temp_dictionary:
        var = high_temp_dictionary[key]
        high_temp_dictionary[key] = middleterm(var)

    lowest_temperature_cities2018 = []
    highest_temperature_cities2018 = []

    #   appending lowest and highest 5 temperature cities in list.
    for i in range(5):  # doing a loop 5 times
        lowest_temperature_cities2018.append(min(low_temp_dictionary))
        low_temp_dictionary.pop(min(low_temp_dictionary))
        highest_temperature_cities2018.append(max(high_temp_dictionary))
        high_temp_dictionary.pop(max(high_temp_dictionary))

    #   returning data acording to users arguement
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
    #
    global cleaned_data
    regions = ['Ήπειρος', 'Θεσσαλία', 'Θράκη', 'Κρήτη', 'Μακεδονία', 'Ν. Αιγαίου', 'Ν. Ιονίου', 'Πελοπόννησος',
               'Στερεά Ελλάδα']

    n = 2006

    if region not in regions:
        return "Arguement must be a greek region!"

    region_data_2018 = {}
    region_data_nyear = {}

    for i in cleaned_data:  # creating a dictionary with each regions city as key and empty list as value
        if i[1] == region and i[3] == '2018':
            region_data_2018[i[2]] = []
    for i in cleaned_data:
        if i[1] == region and i[3] == str(n):
            region_data_nyear[i[2]] = []

    for i in cleaned_data:
        if i[1] == region and i[3] == "2018":  # similarly to task 3
            var = region_data_2018[i[2]]
            var.append(i[6])
            region_data_2018[i[2]] = var
        if i[1] == region and i[3] == str(n):  # using n variable (default is 2006) in case of making changes to it
            # later
            var2 = region_data_nyear[i[2]]
            var2.append(i[6])
            region_data_nyear[i[2]] = var2

    for i in region_data_2018:  # turning list values into a single decimal temperature (middle term)
        var4 = region_data_2018[i]
        var4 = middleterm(var4)
        region_data_2018[i] = var4

    for i in region_data_nyear:  # --- || ----
        var3 = region_data_nyear[i]
        var3 = middleterm(var3)
        region_data_nyear[i] = var3

    for i in region_data_2018:  # printing 2018 citiy and temp, n year and temp, and their difference, according to which year is hotter.
        if i in region_data_nyear:
            if region_data_2018[i] > region_data_nyear[i]: # if else because we dont want any negative numbers.
                print("2018 " + str(i) +" temperature is: "+ str(region_data_2018[i]) + ". Temperature in " + str(n) + " is: " + str(region_data_nyear[i])  + ". " + i + " was hotter in 2018 by " + str(region_data_2018[i] - region_data_nyear[i]) + " degrees celcius."        )
            elif region_data_2018[i] < region_data_nyear[i]:
                print("2018 " + str(i) +" temperature is: "+ str(region_data_2018[i]) + ". Temperature in " + str(n) + " is: " + str(region_data_nyear[i])  + ". " + i + " was hotter in " + str(n) + " by " + str(region_data_nyear[i] - region_data_2018[i]) + " degrees celcius."        )
            elif region_data_2018[i] == region_data_nyear[i]:  # siga mhn einai me tosa dekadika xaxa
                print("2018 " + str(i) + " temperature is: " + str(region_data_2018[i]) + ". Temperature in " + str(n) + " is: " + str(region_data_nyear[i]) + ". " + "The temperature in those 2 years is excactly the same!")
        else:  # insufficient data case
            print("The temperature of " + str(i) + " in 2018 is: " + str(region_data_2018[i]) + ". Insufficient data for " + str(n) + " ."     )

    return ""