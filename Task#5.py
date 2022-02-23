import csv

# opening data
file = open('greek_weather_data.csv', encoding = "UTF8")

csvreader = csv.reader(file)
dataset = list(csvreader)  # converting to list

global cleaned_data
data = []

# breaking the list into elements
for i in range(len(dataset)):
    i = [element for line in dataset[i] for element in line.split('\t')]
    data.append(i)

cleaned_data = data
dataClear = []
for i in range(len(cleaned_data)):
    temp = [cleaned_data[i][3], cleaned_data[i][7]]
    dataClear.append(temp)



# Task 5
y = 0
result = []
for z in range(2006, 2018):
    for i in range(1, len(dataClear)):
        x = dataClear[i][1]
        try:
            x = float(x)
        except:
            continue
        if dataClear[i][0] == str(z):
            if x > y:
                y = x
            result = y
    y = 0
    print(result)

