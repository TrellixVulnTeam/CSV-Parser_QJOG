import csv

# Read csv
with open('team.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

# Parse csv
# Write new csv
