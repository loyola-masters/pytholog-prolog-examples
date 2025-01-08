def parse_prolog_file(file_path):
    clauses = []

    # Read the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Process each line to extract individual clauses
    current_clause = ""
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace
        if line and not line.startswith("%"):  # Ignore empty lines and comments
            if line.endswith('.'):  # Check if the line ends with a dot
                current_clause += line[:-1]  # Remove the dot and append to the current clause
                clauses.append(current_clause)  # Add the completed clause to the list
                current_clause = ""  # Reset the current_clause for the next clause
            else:
                current_clause += line  # Append the line to the current clause

    return clauses
'''
# Example usage:
clauses = read_clauses_from_file("kb.pl")
print(clauses)
'''