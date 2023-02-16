import csv

filename = "ashik.csv"  # Replace with the name of your CSV file
columns = ["Name", "City"]  # Replace with the names of the columns you want to read

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    # Print the header row
    print(reader.fieldnames)
    for row in reader:
        for column in columns:
            column_without_space = column.strip()
            print(f"{column}: {row[column_without_space]}")

# import csv
# from prettytable import PrettyTable
#
# filename = "ashik.csv"  # Replace with the name of your CSV file
# columns = ["Name", "Age", "City", "Occupation"]  # Replace with the names of the columns in your file
#
# # Create a new table object
# table = PrettyTable()
#
# # Add the column names to the table
# table.field_names = columns
#
# with open(filename, "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         # Try to add each row of data to the table
#         try:
#             table.add_row([row[column] for column in columns])
#         except KeyError:
#             print("Missing column in CSV file")
#             break
#
# # Set the table style and print the table
# table.align = "l"
# print(table)

