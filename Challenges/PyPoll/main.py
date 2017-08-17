import os
import csv

DataPath = "."
Files = []
Count = 0
Winner = " "
Total = 0
Votes = {}

for file in os.listdir(DataPath):
	if file.endswith(".csv"):
		Files.append(os.path.join(DataPath, file))


for file in Files:
	with open(file) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			Total += 1
			key = row['Candidate']
			if key in Votes:
				Votes[key] += 1
			else:
				Votes[key] = 1

print("Election Results")
print("---------------------")
print(f"Total Votes: {Total}")
print("---------------------")

for i,j in Votes.items():
	Totes = round(round((int(j)/int(Total)),2)*100,2)
	if Totes > Count:
		Count = Totes
		Winner = i
	print(f"{i}: {Totes}% ({j}) ")
print("---------------------")
print(f"Winner: {Winner}")

Output = "Polldata.txt"
with open(Output, 'w') as poll:
    poll.write('Election Results\n')
    poll.write('---------------------\n')
    poll.write(f"Total Votes: {Total}\n")
    for i,j in Votes.items():
    	Totes = round(round((int(j)/int(Total)),2)*100,2)
    	poll.write(f"{i}: {Totes}% ({j})\n")
    poll.write("----------------------\n")
    poll.write(f"Winner: {Winner}\n")