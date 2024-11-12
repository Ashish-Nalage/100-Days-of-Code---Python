# Python Essentials: Beginner Level (Days 1-15) Documentation

## 1. Basic Python Syntax
- **`print()`**: Displays text or variables.
- **`input()`**: Takes user input as a string.
- **f-Strings**: Format strings using `{}`.
```python
name = input("Enter your name: ")
age = 20
print(f"My name is {name} and I am {age} years old.")
```

## 2. Data Types & Type Conversion
- **Data Types**: 
  - `str`: String, `int`: Integer, `float`: Float, `bool`: Boolean
  - Conversion: `int()`, `float()`, `str()`
```python
num = "10"
num_int = int(num)
print(type(num_int))  # <class 'int'>
```
- **String Methods**:
  - `.lower()`, `.upper()`, `.strip()`, `.split()`, `.replace()`
```python
text = "  Hello World  "
print(text.strip().lower())  # "hello world"
```

## 3. Operators and Expressions
- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `and`, `or`, `not`
```python
result = (5 + 3) * 2  # 16
is_equal = (5 == 5) and (5 != 6)  # True
```

## 4. Control Flow: Conditional Statements
- **if, elif, else**:
```python
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

## 5. Loops
- **For Loop**: Iterates over a sequence (e.g., list, range).
```python
for i in range(3):
    print(i)  # 0, 1, 2
```
- **While Loop**: Repeats as long as a condition is `True`.
```python
count = 0
while count < 3:
    print(count)
    count += 1
```

## 6. Functions

- **Defining Functions**: Use the `def` keyword to define a function, followed by its name and parameters (if any).
- **With Input**: Accept parameters (inputs) to work with when the function is called.
- **With Output**: Use `return` to send back a result from the function.

### Example of Function Definition and Calling

```python
def greet(name):
    """Returns a greeting message for the given name."""
    return f"Hello, {name}!"

# Calling the function with the argument "Alice"
print(greet("Alice"))  # Output: "Hello, Alice!"
```

- **Docstrings**: Used to describe the function’s purpose.
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```
### Key Points:
- Functions are reusable blocks of code that can accept inputs and return outputs.
- Always use meaningful names for functions and parameters.
- Add docstrings for clarity, especially in larger projects, to improve code readability.


## 7. Data Structures
- **Lists**:
  - Creation: `my_list = [1, 2, 3]`
  - Methods: `.append()`, `.remove()`, `.pop()`, `.insert()`, `.sort()`
```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # [1, 2, 3]
```
- **Dictionaries**:
  - Creation: `my_dict = {"name": "Alice", "age": 25}`
  - Access: `my_dict["name"]`
  - Methods: `.keys()`, `.values()`, `.items()`
```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict.keys())  # dict_keys(['name', 'age'])
```

## 8. Built-in Functions
- **`len()`**: Returns the length of a sequence.
- **`range()`**: Generates a sequence of numbers.
- **`type()`**: Returns the type of an object.
- **`round()`**: Rounds a number to a specified number of decimal places.
```python
print(len("Hello"))  # 5
print(list(range(3)))  # [0, 1, 2]
print(type(3.14))  # <class 'float'>
print(round(3.14159, 2))  # 3.14
```

## 9. Modules and Randomization
- **Importing Modules**:
```python
import random
```
- **Random Functions**:
  - `random.randint(a, b)`: Returns a random integer between `a` and `b`.
  - `random.choice(sequence)`: Returns a random element from a sequence.
  - `random.sample(population, n)`: Returns a list of `n` unique random elements.
```python
print(random.randint(1, 10))  # Random integer between 1 and 10
choices = ['apple', 'banana', 'cherry']
print(random.choice(choices))  # Randomly selects one item
```

## 10. Error Handling Basics
- **Using `try-except`**: Catch and handle exceptions to prevent program crashes.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
```


