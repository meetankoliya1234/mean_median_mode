import csv
from collections import Counter

with open('SOCR-HeightWeight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#Mean

mea = len(new_data)
total = 0
for x in new_data:
    total += x

mean = total / mea

#Median

med = len(new_data)
new_data.sort()

if med % 2 == 0:
    median1 = float(new_data[med//2])
    median2 = float(new_data[med//2 - 1])
    median = (median1 + median2)/2
else:
    median = new_data[med//2]

#Mode

data = Counter(new_data)
mode_data_for_range = {
    "75-85": 0,
    "85-95": 0,
    "95-105": 0
}
for weight, occurence in data.items():
    if 50 < float(weight) < 60:
        mode_data_for_range["75-85"] += occurence
    elif 60 < float(weight) < 70:
        mode_data_for_range["85-95"] += occurence
    elif 70 < float(weight) < 80:
        mode_data_for_range["95-105"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in mode_data_for_range.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)

#print

print("Mean is: " + str(mean))
print("Median is: " + str(median))
print(f"Mode is -> {mode:2f}")