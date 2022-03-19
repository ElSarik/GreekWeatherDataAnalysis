from functions.dataset import dataset_open, dataset_split
from functions.dataset_api import get_highest_temperature_by_year, get_highest_amount_of_rain
from functions.dataset_api import five_highestorlowest_temperature_cities_in2018, middleterm_of_place_in_2006_and_2018

dataset = dataset_open()
data = dataset_split(dataset)



get_highest_temperature_by_year(2008, 2010)              #task 3
print("=====================")
get_highest_temperature_by_year()                        #task 3
print("=====================")
get_highest_amount_of_rain()                             #task 4
print("=====================")
print(five_highestorlowest_temperature_cities_in2018())  #task 5
print("=====================")
print(middleterm_of_place_in_2006_and_2018('Μακεδονία')) #task 6
print("=====================")
print(middleterm_of_place_in_2006_and_2018("Ν. Αιγαίου"))