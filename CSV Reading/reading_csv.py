import csv
import os

path = os.path.join(os.getcwd(),"CSV Reading","titan.txt")

with open(path) as f:
    csv_f = csv.reader(f)
    for row in csv_f:
        print(row)

path = os.path.join(os.getcwd(),"CSV Reading","gear+header.csv")
with open(path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)