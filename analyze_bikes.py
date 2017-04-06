# -*- coding: utf-8 -*-

'''
This file parses the 'files-new.csv' CSV file in Pandas, hence showing how
such data can be manipulated in a low level way instead of relying on existing
libraries.
'''

# First, get the data as a string from the file:
raw_data = open('C:\\Users\\Myself\\Playground/PythonTraining/SpyderProject/bikes-new.csv',
                encoding='utf-8').read()

# Split lines of the CSV data
data_lines = raw_data.split('\n')

# print the first three lines
print(data_lines[:3])

# header is the first line of the CSV
headers = data_lines[0]
headers = headers.split(',')

# rows are all but the first line of the CSV
rows = data_lines[1:]

# our goal is to build a dictionnary structure like the following,
# so we can apply column-based operations on it:
#{
#     'Area 1': [20, 32, 14, 20],
#     'Area 2': [12, 41, 11, 9],
#}

# remove the date and time values from the headers
headers = headers[2:]

# We want to create an 'empty' result with the following
# look. We will populate the values later when parsing the rows:
# {
#     'Area 1': [],
#     'Area 2': [],
# }
result = {}
# Add all areas to the result with empty values list 
for header in headers:
    # add a new area with an empty list as value
    result[header] = []

print('Empty result is', result)

# process each row, adding values to the corresponding values in the result
for row in rows:
    values = row.split(',')
    # remove the date and time values from the row
    values = values[2:]
    # transform values into integers
    new_values = []
    for value in values:
        if value != '':
            # convert from string to integer
            new_values.append(int(value))
        else:
            new_values.append(0)
    # or new style to achieve the same result
    new_values_2 = [int(i) if i != '' else 0
                    for i in values]
    print('--- row', new_values)
    for index, value in enumerate(new_values):
        # get header for value
        header = headers[index]
        print(value, 'at', index, 'for', header)
        result[header].append(value)
        
print('Result', result)

print('Total number of bikes from Berri1', 
      sum(result['Berri1']))

# print total number for all areas
for header in headers:
    print('Total number of bikes from {}:'.format(header), 
      sum(result[header]))