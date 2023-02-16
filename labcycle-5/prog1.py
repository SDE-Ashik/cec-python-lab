filename = "example.txt"  # Replace with the name of your file
lines = []

with open(filename, "r") as file:
    for line in file:
        lines.append(line.strip())

print(lines)
