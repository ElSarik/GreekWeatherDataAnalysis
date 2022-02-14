import csv

def dataset_open():
    '''Opens the csv file,
    
       Returns csv content as a 2D list.'''

    #reading the file
    file = open('greek_weather_data.csv', encoding="utf8")
    csvreader = csv.reader(file)
    dataset = list(csvreader)

    return dataset
