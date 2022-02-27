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

#task6
y = 0
dataClear2 = []
for i in range(1, len(cleaned_data)):
    temp = [cleaned_data[i][1], cleaned_data[i][2], cleaned_data[i][3], cleaned_data[i][4], cleaned_data[i][5], cleaned_data[i][13]]
    dataClear2.append(temp)

for z in range(1, len(dataClear2)):
    x = dataClear2[z][5]
    try:
        x = float(x)
    except:
        continue
    if x > y:
        y = x
        result = [dataClear2[z][0], dataClear2[z][1], dataClear2[z][2], dataClear2[z][3], dataClear2[z][4], dataClear2[z][5], ]

print(result)