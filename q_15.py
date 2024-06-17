import csv
filename = 'C:/Users/Admin/Downloads/greenhouse.csv'
data = []
with open(filename, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        data.append(row)
for row in data:
    print(row)
