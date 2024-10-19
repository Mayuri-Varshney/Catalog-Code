# Catalog-Code
Polynomial Secret Finder
This Python script reads a JSON file containing polynomial roots encoded in various bases and computes the constant term (secret, 
𝑐
c) of the polynomial.

Features
Parses input from a JSON file.
Decodes roots from different bases to base 10.
Computes and outputs the constant term.
Usage
Input Format: The input JSON should look like this:

json
Copy code
{
    "keys": {"n": 10, "k": 7},
    "1": {"base": "6", "value": "13444211440455345511"},
    "2": {"base": "15", "value": "aed7015a346d63"},
    ...
}
Run the Script:

bash
Copy code
python polynomial_secret_finder.py
Output: The constant term (secret) will be printed:

php
Copy code
Secret (constant term): <value>
Requirements
Python 3.x
How It Works
The script decodes each root from its specified base and computes the constant term as the product of the decoded values.
