import json

# Function to read JSON file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Example: Assuming the JSON file is named 'test_case.json'
file_path = 'test_case.json'
test_case_data = read_json_file(file_path)

# Print the parsed data
print(test_case_data)



# for decoding values
def decode_values(data):
    decoded_values = {}
    
    for key, value_data in data.items():
        if key.isdigit():  # Process only the numeric keys
            base = int(value_data['base'])
            encoded_value = value_data['value']
            
            # Convert the encoded value to base 10
            decoded_value = int(encoded_value, base)
            decoded_values[key] = decoded_value
    
    return decoded_values

# Decode the y-values from the parsed JSON data
decoded_y_values = decode_values(test_case_data)

# Print the decoded values
print("Decoded values:", decoded_y_values)



#finding the secret c

import json

# Step 1: Read and parse the JSON input from the file
def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Step 2: Decode the values using the provided base
def decode_values(data):
    decoded_values = {}
    for key, value_data in data.items():
        if key.isdigit():  # Process only the numeric keys
            base = int(value_data['base'])
            encoded_value = value_data['value']
            
            # Convert the value from the specified base to base 10
            decoded_value = int(encoded_value, base)
            decoded_values[int(key)] = decoded_value
    return decoded_values

# Step 3: Calculate the constant term of the polynomial (Lagrange Interpolation)
# Here, we'll compute the product of the decoded roots as the constant term.
def find_constant_term(decoded_values):
    product = 1
    for root in decoded_values.values():
        product *= root
    return product

# Step 4: Process both test cases and print the results
def process_test_cases(file_paths):
    for file_path in file_paths:
        # Read the test case
        data = read_json_file(file_path)
        
        # Decode the y-values from the JSON data
        decoded_values = decode_values(data)
        
        # Calculate the constant term using the decoded roots
        constant_term = find_constant_term(decoded_values)
        
        # Print the result (constant term)
        print(f"Secret (constant term) for test case {file_path}: {constant_term}")


