from functions.dataset import dataset_open, dataset_split, five_highestorlowest_temperature_cities_in2018
from functions.dataset import dataset_open, dataset_split, five_highestorlowest_temperature_cities_in2018, middleterm_of_place_in_2006_and_2018
from functions.display import display_row_with_titles

print("Loading...\n\n\n")


dataset = dataset_open()
data = dataset_split(dataset)



print(middleterm_of_place_in_2006_and_2018("Ν. Αιγαίου"))
