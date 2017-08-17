import os
import csv

Months = 0
Revenue = 0
Avg = " "
Increase = 0
IncreaseDate = " "
Decrease = 0
DecreaseDate = " "
Files = []

Path = os.path.join(os.getcwd(), "..")
DataPath = os.path.join(Path, "PyBank")
for file in os.listdir(DataPath):
	if file.endswith(".csv"):
		Files.append(os.path.join(DataPath, file))

for file in Files:
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			Months += 1
			Revenue += int(row['Revenue'])
			if Decrease == 0:
				Decrease = int(row['Revenue'])
				DecreaseDate = row['Date']
			elif int(row['Revenue']) < Decrease:
				Decrease = int(row['Revenue'])
				DecreaseDate = row['Date']
			if Increase == 0:
				Increase = int(row['Revenue'])
				IncreaseDate = row['Date']
			elif int(row['Revenue']) > Increase:
				Increase = int(row['Revenue'])
				IncreaseDate = row['Date']

Avg = round(Revenue/Months,0)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {Months}")
print(f"Total Revenue: ${Revenue}")
print(f"Average Revenue Change: ${Avg}")
print(f"Greatest Increase in Revenue: {IncreaseDate}, $({Increase})")
print(f"Greatest Decrease in Revenue: {DecreaseDate}, $({Decrease})")

Output = "Revenue.txt"
with open(Output, 'w') as bank:
    bank.write('Financial Analysis\n')
    bank.write('---------------------\n')
    bank.write(f"Total Months: {Months}\n")
    bank.write(f"Total Revenue: ${Revenue}\n")
    bank.write(f"Average Revenue Change: ${Avg}\n")
    bank.write(f"Greatest Increase in Revenue: {IncreaseDate}, $({Increase})\n")
    bank.write(f"Greatest Decrease in Revenue: {Decrease}, $({DecreaseDate})\n")