import csv
with open('height-weight.csv',newline='') as f:   
    reader = csv.reader(f) 
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    hight = file_data [i][1]
    new_data.append(float(hight))

sum = 0 
for x in new_data:
    sum = sum + x

n = len(new_data)

print(sum/n)