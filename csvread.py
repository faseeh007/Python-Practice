import csv
with open('example.csv') as File:
    reader=csv.reader(File)
    for rows in reader:
        print(rows)
#dict Reader
results=[]
with open('example.csv') as File:
    reader=csv.DictReader(File)
    for rows in reader:
        results.append(rows)
    print(results)
