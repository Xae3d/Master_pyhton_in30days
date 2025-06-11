## 🔹 1. Python Operators

Operators are symbols used to perform operations on variables and values.

### 🧮 Types of Operators:

| Operator Type      |   Description                 |  Example             |
|--------------------|-------------------------------|----------------------|
| **Arithmetic**     | Perform basic math operations | `+ - * / % // **`   |
| **Assignment**     | Assign values to variables    | `= += -= *= /=`     |
| **Comparison**    | Compare values, return `True`/`False`| `== != > < >=<=` |
| **Logical**       | Combine conditions             | `and or not`        |
| **Bitwise**       | Bit-level operations           | `& | ^ ~ << >>`     |
| **Membership**    | Test if value exists in a sequence  | `in`, `not in` |
| **Identity**      | Test object identity           | `is`, `is not`      |

### 🔹 Example: Arithmetic Operators
```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a % b)   # 1 (remainder)
print(a // b)  # 3 (floor division)
print(a ** b)  # 1000 (10^3)

🔹 2. Type Conversion
Changing data from one type to another.

🛠️ Types:
Type	 Example	        Converts To
int()	 int("10")	      Integer
float()	 float("3.14")	  Float
str()	 str(100)	      String
bool()	 bool(1)	      Boolean

🔹 Type Casting vs. Type Conversion
Type Casting: Manual conversion using functions like int(), float(), str()

Type Conversion: Automatic conversion done by Python (e.g. int + float = float)

x = "5"
y = int(x)   # Casting string to int
print(type(y))  # <class 'int'>


🔹 3. User Input in Python
Takes input from the user during program execution.

📥 Using input() function

name = input("Enter your name: ")
print("Hello", name)


🔁 Input is always string!
To use it as int or float, convert it:

age = int(input("Enter your age: "))
pi = float(input("Enter value of pi: "))


✅ Summary
** Mastered different types of Python operators

** Learned how to cast and convert data types

** Practiced taking user input and using it in programs