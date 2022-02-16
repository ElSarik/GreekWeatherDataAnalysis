import random
# Displaying data in format: column_title = row_data
def display_row_with_titles(data: 'list[list[str]]', row_indexes: list = [1]):
    '''Prints arg2 indexes of arg1 list together with arg1[0] titles,
       
       arg1: 2D str(list),
       arg2 (optional): int(list) of arg1 indexes to be printed,
       
       Returns None.'''

    column_titles = data[0]

    for row_index in row_indexes:
        row_data = data[row_index]

        for index in range (0, len(column_titles)):
            print(f'{index + 1} - {column_titles[index]} = {row_data[index]}')

        print("============================================================")

