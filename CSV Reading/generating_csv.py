import csv
import os

all_gear = [['Jean Gear','AirJet','FireArm','AirArm'],
['Goh Gear','AirJet','WaterArm','AirArm'],
['Julia Gear','FireJet','FireArm Both','']]

all_gear_dict = []

for user in all_gear:
    temp_dict = {
        'name':user[0],
        'Ramjet Engine':user[1],
        'Left Arm':user[2],
        'Right Arm':user[3]
    }
    all_gear_dict.append(temp_dict)

path = os.path.join(os.getcwd(),"CSV Reading","gear.csv")

with open(path,'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(all_gear)

path = os.path.join(os.getcwd(),"CSV Reading","gear+header.csv")
with open(path,'w') as csv_file:
    dictwriter = csv.DictWriter(csv_file,list(temp_dict.keys()))
    dictwriter.writeheader()
    dictwriter.writerows(all_gear_dict)