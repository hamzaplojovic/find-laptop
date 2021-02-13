import csv
data = {}
f = open('cpu.csv')
reader = csv.reader(f)
for x in reader:
    data[x[3]] = x[5]
print(data)

f.close()