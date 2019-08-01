import csv
with open("C:/khushipyythonn/newcsv.csv")as f
    data=csv.DictReader(f)
    for row in data:
        print(row)
