import csv

# Define a dictionary with some sample data
my_dict = {"Name": "Ashik", "Age": 22, "City": "New York", "Occupation": "CEO"}

# Define the name of the CSV file
filename = "my_csv_file.csv"

# Write the dictionary to the CSV file
with open(filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=my_dict.keys())
    writer.writeheader()
    writer.writerow(my_dict)

# Read the CSV file and display its contents
with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        for key, value in row.items():
            print(f"{key}: {value}")
