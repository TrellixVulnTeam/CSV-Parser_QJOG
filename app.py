import csv


# # Read csv
with open('team.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)


# # Write new csv
    with open('new_names.csv', 'w') as new_file:

        csv_writer = csv.DictWriter(new_file, delimiter='\t')

        # csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
