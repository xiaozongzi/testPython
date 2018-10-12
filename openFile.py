import csv
import pandas
file = pandas.read_csv(open('Indian Liver Patient Dataset (ILPD).csv'))
# file = csv.reader(open('epi_r.csv'))
# print(file.head(10))

data = file[3:8]

# print(data.groupby("65").sum())
print(data)
# print(file[1][1])
# for raw in file:
#     print(file.line_num, raw)
