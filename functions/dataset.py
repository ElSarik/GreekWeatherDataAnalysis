import csv

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

    data = []

    #breaking the list into elements
    for i in range(len(dataset)):
        i = [element for line in dataset[i] for element in line.split('\t')]
        data.append(i)

    return data
