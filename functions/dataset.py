import csv
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

 #-------------vandls work-----------------------------------------------------------------------------#



def five_cities_with_lower_temperature_middleterm_in2018():
    #made by vandl
    #each row of CSV looks like:
    # ['33', 'Ήπειρος', 'Αγία Κυριακή Ιωαννίνων', '2018', '11', '3', '15.6', '26.3', '13:50:00', '7.4', '06:30:00', '4.7', '1.9', '0.0', '2.7', '25.7', '13:20:00', 'E', '515.0', '"39° 31\' 27"" N"', '"20° 52\' 55"" E"', '39.524167','20.881944']
    #MEAN_TEMP	HIGH_TEMP, indexes: 6 ,7

    #task
    # #3. Να βρείτε τις 5 πόλεις/χωριά με τον υψηλότερο και χαμηλότερο μέσο όρο θερμοκρασιών για το 2018

    global cleaned_data

    #filteringdata
    data_in2018 = []
    for i in cleaned_data:
        if i[3] == "2018":
            data_in2018.append(i)
        else:
            continue
    #data_in2018 now has CSV rows only from year 2018

    #WARINGING! headers NOT included in data_in2018!!!!!

    exceptions = []
    cities_and_temperatures__dictionary  = {}
    index = 0
    #to find middle term of termperatures in a city, we have to find middle term in 1 day, each day we have data of in 1 city,
    # because we get min and max value of temp in 1 day.
    for i in data_in2018:
        #using try except because some data is missing, so if data not found dont append anything in dictionary
        try:
            #appending in dictionary the city, day, month and DAILY middle term of each city each different day.
            cities_and_temperatures__dictionary[i[2] + " " + i[4] + "/" + i[5]] = "{:.2f}".format((float(i[6]) + float(i[7])) / 2)
            index += 1
        except:
            exceptions.append(i)
    return  cities_and_temperatures__dictionary["Επταπύργιο Θεσσαλονίκης 10/4"]