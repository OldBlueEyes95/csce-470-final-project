def remove_duplicates(input_file, output_file):
    seen = set()
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line not in seen:
                outfile.write(line)
                seen.add(line)

# Specify your file names
input_file = 'many.txt'   # Replace with your actual file name
output_file = 'all.txt'   # The name for the new file

remove_duplicates(input_file, output_file)