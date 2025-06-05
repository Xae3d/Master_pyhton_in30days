# 📅 Day 2 – Python Operators, Type Conversion & User Input

**Date:** June 4, 2025  
**Topics Covered:**  
- Operators in Python  
- Types of Operators  
- Type Conversion vs Type Casting  
- Taking Input from Users  

---

## 🧮 Operators in Python

Operators are special symbols used to perform operations on variables and values.

### ✅ Types of Operators:

1. **Arithmetic Operators**
   - `+` Addition  
   - `-` Subtraction  
   - `*` Multiplication  
   - `/` Division  
   - `//` Floor Division  
   - `%` Modulus (remainder)  
   - `**` Exponent (power)

   #### Example:
   ```python
   a = 10
   b = 3
   print(a + b)  # 13
   print(a / b)  # 3.33
   print(a // b) # 3
   print(a ** b) # 1000

2. ### Assignment Operators
=
+=, -=, *=, /=, etc.

Example:
x = 5
x += 2  # same as x = x + 2
print(x)  # 7
3. ### Comparison (Relational) Operators

==, !=, >, <, >=, <=

Example:
print(5 > 3)  # True
print(5 == 5) # True

4. ### Logical Operators
and, or, not

Example:
a = 10
b = 5
print(a > 3 and b < 7)  # True
print(not(a < b))       # True
Bitwise Operators (Used for binary operations)

&, |, ^, ~, <<, >>

🔄 Type Conversion and Casting
🔁 Type Conversion (Automatic)
Python automatically converts one data type to another when needed.

Example:
x = 5     # int
y = 2.5   # float
z = x + y
print(z)        # 7.5 (float)
print(type(z))  # <class 'float'>

🎯 Type Casting (Manual)
You can manually change one data type into another using functions like:

int(), float(), str(), bool()

Example:
a = "10"
b = int(a)  # now b is an integer
print(b + 5)  # 15
⌨️ Taking Input from User
Use input() function to get user input (always returns a string).

🧠 Summary
Learned different types of operators

Understood automatic type conversion and manual type casting

Practiced taking user input and converting input types

✅ I'm getting more comfortable with Python syntax and logic.
