import csv
import re
from pprint import pprint


global cleaned_data

def dataset_open():
    '''Opens the csv file,
    
       Returns csv content as a 2D list.'''

    #reading the file
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

    #breaking the list into elements
    for i in range(len(dataset)):
        i = [element for line in dataset[i] for element in line.split('\t')]
        data.append(i)

    cleaned_data = data

    return data

    #    -------------vandls work-----------------------------------------------------------------------------#



def five_cities_with_lower_temperature_middleterm_in2018():
    #   made by vandl
    #   each row of CSV looks like:
    #    ['33', 'Ήπειρος', 'Αγία Κυριακή Ιωαννίνων', '2018', '11', '3', '15.6', '26.3', '13:50:00', '7.4', '06:30:00', '4.7', '1.9', '0.0', '2.7', '25.7', '13:20:00', 'E', '515.0', '"39° 31\' 27"" N"', '"20° 52\' 55"" E"', '39.524167','20.881944']
    #   0          1           2                       3     4     5      6    7           8         9        10   .   .
    #   MEAN_TEMP	HIGH_TEMP, indexes: 6 ,7

    #   task
    #   #3. Να βρείτε τις 5 πόλεις/χωριά με τον υψηλότερο και χαμηλότερο μέσο όρο θερμοκρασιών για το 2018

    global cleaned_data

    #   filteringdata
    data_in2018 = []
    for i in cleaned_data:
        if i[3] == "2018":
            data_in2018.append(i)
        else:
            continue
    #   data_in2018 now has CSV rows only from year 2018

    #   WARINGING! headers NOT included in data_in2018!!!!!
    #   creating a list with all cities once
    cities = []
    for i in data_in2018:
        if i[2] not in cities:
            cities.append(i[2])

    # assinging in main list every city's middle temp term, with same index as city in cities list, so we can get
    # data from mainlist.
    indx = 0
    mainlist = []
    helpfullist = []
    for index, i in enumerate(data_in2018):
        # calculating the middle term of every city and appending it to mainlist


        #   using if else because the chain wont work in ONLY first index of data_in2018
        if i == data_in2018[0]:
            i6 = float(i[6])
            i7 = float(i[7])
            #   calculating middle term of each day (each row)
            helpfullist.append((i6 + i7) / 2)

            indx += 1

        #   main program
        else:
            #   using try except because some data is missing
            try:
                i6 = float(i[6])
                i7 = float(i[7])
                #   if the nth city of data_in2018 is the SAME as previous row:
                #   using index manually because I can't figure out how to use enumerate
                if i[2] == data_in2018[indx][2]:
                    helpfullist.append((i6 + i7) / 2)
                    indx += 1


                else:
                    mainlist.append(sum(helpfullist) / len(helpfullist))
                    del helpfullist[:]
                    helpfullist.append((i6 + i7) / 2)
                    indx += 1




            except:
                continue


    return mainlist


