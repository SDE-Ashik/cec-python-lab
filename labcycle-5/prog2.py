input_file = "input.txt"  # Replace with the name of your input file
output_file = "output.txt"  # Replace with the name of your output file

with open(input_file, "r") as in_file, open(output_file, "w") as out_file:
    for i, line in enumerate(in_file):
        if i % 2 == 0:
            out_file.write(line)
