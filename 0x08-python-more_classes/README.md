# Python - More Classes and Objects

This set of Python tasks is designed to help you practice working with classes and objects. Each task builds upon the previous one, adding more features and functionality to a `Rectangle` class.

## Task 0: 0-rectangle.py

- Create an empty class called `Rectangle` that represents a rectangle.

## Task 1: 1-rectangle.py

- Add private instance attributes `width` and `height`.
- Implement getters and setters for `width` and `height`.
- Ensure that `width` and `height` are integers and not negative.

## Task 2: 2-rectangle.py

- Add methods `area()` and `perimeter()` to calculate the area and perimeter of the rectangle.
- Make sure the perimeter is 0 if either `width` or `height` is 0.

## Task 3: 3-rectangle.py

- Implement `__str__` and `__repr__` methods to print and represent the rectangle.
- Use '#' to represent the rectangle in strings.
- Ensure that an empty string is returned if `width` or `height` is 0.

## Task 4: 4-rectangle.py

- Add a class attribute `number_of_instances` to keep track of the number of instances.
- Increment it during each instantiation and decrement during deletion.

## Task 5: 5-rectangle.py

- Add a class attribute `print_symbol` to customize the symbol used for string representation.
- Update `__str__` and `__repr__` to use this symbol.

## Task 6: 6-rectangle.py

- Add a static method `bigger_or_equal` to compare two rectangles based on area.
- Raise TypeError if the input is not a `Rectangle` instance.
- Return the rectangle with the larger area.

## Task 7: 7-rectangle.py

- Add a class method `square` to create a square `Rectangle` with the same width and height.
- Use this method to create square instances.

## Task 8: 8-rectangle.py

- Enhance the `bigger_or_equal` method to return the first rectangle if the areas are equal.

## Task 9: 9-rectangle.py

- Complete the class by adding all previous functionality.
- Improve the class attributes and methods.

## Task 10: 101-nqueens.py

- Solve the N queens puzzle using backtracking.
- Print all possible solutions for a given N on the chessboard.

# Usage:

```
python 101-nqueens.py N
```

- N must be an integer >= 4.
- The program prints solutions to the N queens problem, one per line.
