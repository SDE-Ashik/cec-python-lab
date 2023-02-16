import csv

filename = "ashik.csv"  # Replace with the name of your CSV file

with open(filename, "r") as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

string_list = [", ".join(row) for row in rows]

print(string_list)
