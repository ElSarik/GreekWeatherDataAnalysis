from functions.dataset import dataset_open, dataset_split
from functions.display import display_row_with_titles

dataset = dataset_open()
data = dataset_split(dataset)

###### Optional alternative print using 2nd argument (shows empty fields).
indexes = [92, 93]
display_row_with_titles(data, indexes)

###### Prints with first line of data - without 2nd argument.
# display_row_with_titles(data)