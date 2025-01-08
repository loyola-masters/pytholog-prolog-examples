
# Pytholog: Prolog en Python

Pytholog is a Python library that enables logic programming in Python, mimicking Prolog syntax and backtracking. This project aims to explore ways to combine symbolic reasoning with machine learning.

## Features

- Implements Prolog-like syntax in Python
- Supports probabilistic and logical reasoning
- Uses binary search for efficient fact retrieval
- Includes both a Python library and a command-line tool

## Installation

Install Pytholog using pip:

```bash
pip install pytholog
```

## Usage

Here's a basic example of how to use Pytholog, located in folder `./platon_socrates`:

```python
from pytholog import KnowledgeBase

# Create a knowledge base
kb = KnowledgeBase("family")

# Add facts and rules
kb.add_facts("parent(john, mary)")
kb.add_facts("parent(mary, ann)")
kb.add_rule("grandparent(X, Y) :- parent(X, Z), parent(Z, Y)")

# Query the knowledge base
results = kb.query("grandparent(john, ann)")
print(results)  # Output: [{'X': 'john', 'Y': 'ann'}]
```

## Documentation

For full documentation and more examples, visit the [Pytholog documentation](https://mnoorfawi.github.io/pytholog/)

## Command-line Tool

Pytholog also provides a command-line tool for interactive use and as a RESTful API. For more information, refer to the [Pytholog Tool documentation](https://sourceforge.net/projects/pytholog/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.


# Pytholog US State Coloring Example

This repository demonstrates how to use Pytholog to solve a constraint satisfaction problem for coloring US states.

## Contents

- `city_color.py`: Main Python script that uses Pytholog to query the knowledge base
- `city_color.pl`: Prolog file containing the knowledge base for state coloring
- `prolog_converter.py`: Module for parsing Prolog files into Pytholog-compatible format

The folder structure is as follows:
```
us_states_colors/
    ├── city_color.py
    ├── city_color.pl
    └── prolog_converter/
        ├── __init__.py
        └── prolog_converter.py
```

## Setup

1. Install Pytholog:
   ```bash
   pip install pytholog
   ```

2. Ensure all files are in the same directory

## Usage

Run the main script:

```bash
python city_color.py
```

This will load the Prolog knowledge base, convert it to Pytholog format, and query for a valid coloring of Alabama, Mississippi, Georgia, Tennessee, and Florida.

## Exercise

Try to identify and remove the redundant predicate in the `coloring` rule within `city_color.pl`. After making the change, run the code to validate that it still works correctly.
