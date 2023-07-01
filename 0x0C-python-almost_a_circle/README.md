# Python - Object-Oriented Programming Project

This project demonstrates proficiency in Python object-oriented programming through the implementation of three interconnected classes representing rectangles and squares. A comprehensive test suite has been developed using the `unittest` module to ensure the functionality of each class.

The project utilizes various Python tools and concepts, including:

- Importing modules
- Handling exceptions
- Defining private attributes
- Implementing getter and setter methods
- Working with class and static methods
- Utilizing inheritance
- Performing file input/output (I/O)
- Serializing and deserializing data in JSON and CSV formats
- Conducting unit tests using the `unittest` module

## Tests ✔️

The project includes an independently-developed test suite, located in the `tests/test_models` folder. It consists of the following test files:

- [test_base.py](./tests/test_models/test_base.py)
- [test_rectangle.py](./tests/test_models/test_rectangle.py)
- [test_square.py](./tests/test_models/test_square.py)

## Classes 🆑

### Base

The `Base` class serves as the foundation for all other classes in the project. It encompasses the following features:

- Private class attribute `__nb_objects = 0`.
- Public instance attribute `id`.
- Class constructor `def __init__(self, id=None):`
  - If `id` is `None`, it increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  - Otherwise, it sets the public instance attribute `id` to the provided `id`.
- Static method `def to_json_string(list_dictionaries):` that returns the JSON string serialization of a list of dictionaries.
  - If `list_dictionaries` is `None` or empty, it returns the string `"[]"`.
- Class method `def save_to_file(cls, list_objs):` that writes the JSON serialization of a list of objects to a file.
  - The parameter `list_objs` is expected to be a list of instances inherited from `Base`.
  - If `list_objs` is `None`, the function saves an empty list.
  - The file is saved with the name `<cls name>.json` (e.g., `Rectangle.json`).
  - If the file already exists, it overwrites the existing file.
- Static method `def from_json_string(json_string):` that returns a list of objects deserialized from a JSON string.
  - The parameter `json_string` is expected to be a string representing a list of dictionaries.
  - If `json_string` is `None` or empty, the function returns an empty list.
- Class method `def create(cls, **dictionary):` that instantiates an object with the provided attributes.
  - It creates an instance with the attributes given in `**dictionary`.
- Class method `def load_from_file(cls):` that returns a list of objects instantiated from a JSON file.
  - It reads from the JSON file `<cls name>.json` (e.g., `Rectangle.json`).
  - If the file does not exist, the function returns an empty list.
- Class method `def save_to_file_csv(cls, list_objs):` that writes the CSV serialization of a list of objects to a file.
  - The parameter `list_objs` is expected to be a list of instances inherited from `Base`.
  - If `list_objs` is `None`, the function saves an empty list.
  - The file is saved with the name `<cls name>.csv` (e.g., `Rectangle.csv`).
  - Objects are serialized in the format `<id>,<width>,<height>,<x>,<y>` for `Rectangle` objects and `<id>,<size>,

<x>,<y>`for`Square` objects.

- Class method `def load_from_file_csv(cls):` that returns a list of objects instantiated from a CSV file.
  - It reads from the CSV file `<cls name>.csv` (e.g., `Rectangle.csv`).
  - If the file does not exist, the function returns an empty list.
- Static method `def draw(list_rectangles, list_squares):` that draws `Rectangle` and `Square` instances in a GUI window using the `turtle` module.
  - The parameter `list_rectangles` is expected to be a list of `Rectangle` objects to be displayed.
  - The parameter `list_squares` is expected to be a list of `Square` objects to be displayed.

### Rectangle

The `Rectangle` class represents a rectangle and inherits from the `Base` class. It includes the following features:

- Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  - Each private instance attribute has its own getter and setter methods.
- Class constructor `def __init__(self, width, height, x=0, y=0, id=None):`
  - If any of `width`, `height`, `x`, or `y` is not an integer, it raises a `TypeError` exception with the message `<attribute> must be an integer`.
  - If either `width` or `height` is less than or equal to 0, it raises a `ValueError` exception with the message `<attribute> must be > 0`.
  - If either `x` or `y` is less than 0, it raises a `ValueError` exception with the message `<attribute> must be >= 0`.
- Public method `def area(self):` that returns the area of the `Rectangle` instance.
- Public method `def display(self):` that prints the `Rectangle` instance to the standard output (`stdout`) using the `#` character.
  - It prints new lines for the `y` coordinate and spaces for the `x` coordinate.
- Overridden `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`.
- Public method `def update(self, *args, **kwargs):` that updates an instance of a `Rectangle` with the given attributes.
  - The `*args` arguments must be supplied in the following order:
    - 1st: `id`
    - 2nd: `width`
    - 3rd: `height`
    - 4th: `x`
    - 5th: `y`
  - The `**kwargs` argument is expected to be a double pointer to a dictionary of new key/value attributes to update the `Rectangle` with.
  - The `**kwargs` argument is skipped if `*args` exists.
- Public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle` instance.

### Square

The `Square` class represents a square and inherits from the `Rectangle` class. It includes the following features:

- Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  - The `width` and `height` of the superclass `Rectangle` are assigned using the value of `size`.
- Overridden `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
- Public method `def update(self, *args, **kwargs):` that updates an instance of a `Square` with the given attributes.
  - The `*args`

arguments must be supplied in the following order:
_ 1st: `id`
_ 2nd: `size`
_ 3rd: `x`
_ 4th: `y`

- The `**kwargs` argument is expected to be a double pointer to a dictionary of new key/value attributes to update the `Square` with.
- The `**kwargs` argument is skipped if `*args` exists.
- Public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`.

This project showcases a strong understanding of Python's object-oriented programming principles and their practical application in building modular and reusable code.
