# Python Input/Output Project

This Python project focuses on input and output operations in Python. It includes several Python scripts that demonstrate various file handling and text processing techniques.

## Files and Descriptions

### 1. 0-read_file.py

This script defines a function `read_file(filename="")` that reads a text file (UTF8) and prints its contents to stdout. The function uses the `with` statement for file handling.

### 2. 1-number_of_lines.py

This script defines a function `number_of_lines(filename="")` that returns the number of lines in a text file. It also uses the `with` statement for file handling.

### 3. 2-read_lines.py

The `2-read_lines.py` script defines a function `read_lines(filename="", nb_lines=0)` that reads a specified number of lines from a text file and prints them to stdout. It uses the `with` statement for file handling.

### 4. 3-write_file.py

This script defines a function `write_file(filename="", text="")` that writes a string to a UTF8 text file. It returns the number of characters written and uses the `with` statement for file handling.

### 5. 4-append_write.py

The `4-append_write.py` script defines a function `append_write(filename="", text="")` that appends a string to the end of a UTF8 text file. It returns the number of characters appended and uses the `with` statement for file handling.

### 6. 5-to_json_string.py

This script defines a function `to_json_string(my_obj)` that returns the JSON representation of a Python object using the `json` module.

### 7. 6-from_json_string.py

The `6-from_json_string.py` script defines a function `from_json_string(my_str)` that converts a JSON string into a Python object using the `json` module.

### 8. 7-save_to_json_file.py

This script defines a function `save_to_json_file(my_obj, filename)` that writes a Python object to a text file in JSON format using the `json` module.

### 9. 8-load_from_json_file.py

The `8-load_from_json_file.py` script defines a function `load_from_json_file(filename)` that creates a Python object from a JSON file using the `json` module.

### 10. 9-add_item.py

This script adds all command-line arguments to a Python list and saves them to a JSON file. It demonstrates how to use the `json` module for reading and writing JSON files.

### 11. 10-class_to_json.py

The `10-class_to_json.py` script defines a function `class_to_json(obj)` that returns the dictionary representation of a simple data structure.

### 12. 11-student.py

This script defines a Python class called `Student`, which represents a student with attributes such as first name, last name, and age. It also includes methods for converting the object to JSON format and reloading attributes from a JSON dictionary.

### 13. 12-pascal_triangle.py

The `12-pascal_triangle.py` script defines a function `pascal_triangle(n)` that generates Pascal's Triangle up to a specified number of rows `n`.

### 14. 13-insert_number.py

This script defines a function `insert_number(filename="", search_string="", new_string="")` that inserts text after each line containing a given string in a file. It reads the file, searches for the specified string, and inserts the new string after it.

### 15. 100-append_after.py

The `100-append_after.py` script defines a more advanced version of the text insertion function. It includes docstrings and follows best practices for coding and commenting.

### 16. 101-stats.py

This script reads from standard input and computes statistics after every ten lines or when interrupted (CTRL + C). It calculates the total file size and counts of read status codes.

## Getting Started

To run any of the scripts, follow these steps:

1. Open your terminal.
2. Navigate to the directory where the script is located.
3. Run the script using Python. For example:
   ```
   python 0-read_file.py
   ```

Make sure you have Python installed on your system.
