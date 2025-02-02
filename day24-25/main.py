# import csv
# with open('data.csv') as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         temp.append(row[1])

import pandas
data = pandas.read_csv('data.csv')
# avg_temp = sum(data['temp'].to_list())/len(data['temp'].to_list())
# print(avg_temp)
# print(data['temp'].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'mon']
# monday.temp = (monday.temp * 9 / 5) + 32
# print(monday.temp)  
