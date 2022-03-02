from functions.dataset import dataset_open, dataset_split, get_cleaned_data
from functions.dataset_api import get_data_by_header_list
from functions.display import display_row_with_titles

dataset = dataset_open()
data = dataset_split(dataset)

###### Optional alternative print using 2nd argument (shows empty fields).
# indexes = [92, 93]
# display_row_with_titles(data, indexes)

###### Prints with first line of data - without 2nd argument.
# display_row_with_titles(data)


# data = get_cleaned_data()
# print(data)

header_list = ['YeAr', 'HiGh_tEmP']

data = get_data_by_header_list(header_list)

# data = get_cleaned_data()
for row in range(0, 10):
    print(data[row])