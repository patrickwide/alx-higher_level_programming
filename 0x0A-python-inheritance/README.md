# Python Inheritance and Object Utilities

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the Python Inheritance and Object Utilities project! This project provides a set of Python scripts and utilities that demonstrate and extend the concept of inheritance in Python. It also includes a handy object attribute and method lookup function.

In this project, you'll find various Python scripts that cover topics such as creating custom classes, inheriting from base classes, overriding methods, and working with object attributes. Additionally, we provide a `lookup` function that allows you to inspect objects and retrieve a list of their available attributes and methods.

## Project Structure

Here's an overview of the project structure:

- `0-lookup.py`: The `lookup` function, which returns a list of an object's available attributes and methods.
- `1-my_list.py`: Defines an inherited list class `MyList` with a `print_sorted` method for sorted printing.
- `2-is_same_class.py`: Contains a function `is_same_class` to check if an object is exactly an instance of a given class.
- `3-is_kind_of_class.py`: Contains a function `is_kind_of_class` to check if an object is an instance or inherited instance of a class.
- `4-inherits_from.py`: Contains a function `inherits_from` to check if an object is an inherited instance of a class.
- `5-base_geometry.py`: Defines an empty class `BaseGeometry` to be used as a base class.
- `6-base_geometry.py`: Contains an updated `BaseGeometry` class with an `integer_validator` method.
- `7-base_geometry.py`: Contains a `Rectangle` class that inherits from `BaseGeometry` with an overridden `area` method.
- `8-rectangle.py`: Contains an alternative implementation of the `Rectangle` class.
- `9-rectangle.py`: Contains the `Rectangle` class and the `Square` class that inherits from `Rectangle`.
- `10-square.py` and `11-square.py`: Implementations of the `Square` class with `integer_validator` and `super` usage.
- `100-my_int.py`: Defines a class `MyInt` that inverts the behavior of `==` and `!=` operators.

## Usage

To use this project, you can follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone git@github.com:patrickwide/alx-higher_level_programming.git
   ```

2. Navigate to the project directory:

   ```
   cd alx-higher_level_programming/0x0A-python-inheritance
   ```

3. You can import and use the Python scripts in your own Python projects as needed. Refer to the individual script files for documentation and examples on how to use each utility.

## Examples

Here are some examples of how to use the utilities provided by this project:

### Using the `lookup` function

```python
from lookup import lookup

my_list = [1, 2, 3]
result = lookup(my_list)
print(result)
```

This will output a list of attributes and methods of the `my_list` object.

### Creating a `MyList` instance

```python
from my_list import MyList

my_list = MyList([3, 1, 2])
my_list.print_sorted()
```

This will print the elements of `my_list` in sorted order.
