import json

# Function to read and parse JSON data
def read_json_data(data):
    return data

# Function to decode values from different bases
def decode_values(data):
    decoded_values = {}
    for key, value_data in data.items():
        if key.isdigit():  # Process only numeric keys (roots)
            base = int(value_data['base'])
            encoded_value = value_data['value']
            
            # Convert the value from the specified base to base 10
            decoded_value = int(encoded_value, base)
            decoded_values[int(key)] = decoded_value
    
    return decoded_values

# Function to calculate the constant term of the polynomial
def find_constant_term(decoded_values):
    product = 1
    for root in decoded_values.values():
        product *= root
    return product

# Function to process the input data and compute the result
def process_test_case(data):
    # Parse the input data
    parsed_data = read_json_data(data)
    
    # Decode the values from the specified base
    decoded_values = decode_values(parsed_data)
    
    # Calculate the constant term using the decoded roots
    constant_term = find_constant_term(decoded_values)
    
    # Return the constant term (secret)
    return constant_term

# Example input (test case)
test_case_data = {
    "keys": {
        "n": 10,
        "k": 7
    },
    "1": {
        "base": "6",
        "value": "13444211440455345511"
    },
    "2": {
        "base": "15",
        "value": "aed7015a346d63"
    },
    "3": {
        "base": "15",
        "value": "6aeeb69631c227c"
    },
    "4": {
        "base": "16",
        "value": "e1b5e05623d881f"
    },
    "5": {
        "base": "8",
        "value": "316034514573652620673"
    },
    "6": {
        "base": "3",
        "value": "2122212201122002221120200210011020220200"
    },
    "7": {
        "base": "3",
        "value": "20120221122211000100210021102001201112121"
    },
    "8": {
        "base": "6",
        "value": "20220554335330240002224253"
    },
    "9": {
        "base": "12",
        "value": "45153788322a1255483"
    },
    "10": {
        "base": "7",
        "value": "1101613130313526312514143"
    }
}

# Process the test case and print the result
constant_term = process_test_case(test_case_data)
print(f"Secret (constant term): {constant_term}")
