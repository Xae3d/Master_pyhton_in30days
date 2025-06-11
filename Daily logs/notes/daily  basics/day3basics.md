# 📘 Day 3 Notes – Strings & Conditional Statements

---

## 🔹 1. Python Strings

A **string** is a sequence of characters enclosed in single `' '` or double `" "` quotes.

```python
name = "Saeed Tamboli"

** Strings are immutable — you can’t change its  characters.

  🔹 2. Basic String Operations: 

Operation	          Description	                Example
Concatenation	  Joining strings with +	  "Hello " + "World"
Repetition	      Repeating strings with *	   "Hi" * 3 → HiHiHi
Membership	      Checking substring with in	"a" in "Saeed" → True

a = "Python"
b = "Rocks"

print(a + " " + b)  # Python Rocks
print(a * 2)        # PythonPython
print("P" in a)     # True


🔹 3. Indexing & Slicing: 
-- slicing means cutting a part of something .we can cut out a part of a string,list or tuple etc.

Concept	             Syntax	                 Example
Indexing	       s[index]	            "Hello"[0] → H
Negative Index	    s[-1]	             "Hello"[-1] → o
Slicing	            s[start:end]	     "Hello"[1:4] → ell
Step Slicing	    s[start:end:step]	  "Hello"[::2] → Hlo
  

word = "Tamboli"
print(word[0])       # T
print(word[-1])      # i
print(word[1:5])     # ambo
print(word[::-1])    # ilobmaT (reverse string)

🔹 4. Common String Functions:

Function	  Description	                     Example
len()	      Returns length of string	        len("Saeed") → 5
lower()	      Converts to lowercase	            "PYTHON".lower()
upper()	      Converts to uppercase	            "hello".upper()
strip()	      Removes whitespace	             " hello ".strip()
replace()	  Replaces characters	             "yes".replace("y", "n")
count()	      Counts occurrences	             "apple".count("p") → 2
find()	      Finds index of substring	          "hello".find("l") → 2

msg = "  Python is FUN!  "
print(len(msg))               # 18
print(msg.strip())            # "Python is FUN!"
print(msg.lower())            # "  python is fun!  "
print(msg.replace("FUN", "cool"))  # Python is cool!


🔹 5. Conditional Statements:

Allow your program to make decisions.

✴️ Syntax:

if condition:
    # code block
elif another_condition:
    # another block
else:
    # fallback block

✅ Example:

age = 20

if age < 18:
    print("Minor")
elif age <= 60:
    print("Adult")
else:
    print("Senior Citizen")

🔹 6. Nested Conditions: 
You can use if inside another if block.

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not a positive number")


📌 Summary
-- Strings are sequences; you can slice, index, and manipulate them.

-- String methods help clean and format text.

-- Conditional logic adds decision-making to your code.

-- Nesting conditions helps handle more complex logic.