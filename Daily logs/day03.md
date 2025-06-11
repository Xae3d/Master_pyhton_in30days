# 🐍 Day 3 – Strings & Conditional Statements

📅 **Date:** June 5, 2025  
🕒 **Status:** Completed ✅  
🧠 **Mood:** Super productive and excited! 💡✨

---

## ✅ What I Learned Today

Today was packed with essential concepts that form the backbone of most Python programs:

1. 🔹 **Strings** – Creating and manipulating strings
2. 🔹 **Basic String Operations** – Concatenation, repetition, membership
3. 🔹 **Indexing & Slicing** – Accessing parts of strings
4. 🔹 **String Functions** – `len()`, `.lower()`, `.upper()`, `.replace()`, `.strip()`, etc.
5. 🔹 **Conditional Statements** – `if`, `else`, `elif`, and nested conditions

---

## 📘 Notes Summary

📌 Detailed notes → [notes/day03basics.md](../notes/day03basics.md)

---

## 🧪 Code Snippets

### ✨ Working with Strings

```python
name = "Saeed Tamboli"
print(name[0])           # S
print(name[-1])          # i
print(name[0:6])         # Saeed
print(name.upper())      # SAEED TAMBOLI
print(name.lower())      # saeed tamboli
print(name.replace("e", "3"))  # Sa33d Tamboli

🔁 String Operations: 
a = "Python"
b = "Rocks"

print(a + " " + b)     # Python Rocks
print(a * 3)           # PythonPythonPython
print("P" in a)        # True

------
❓ Conditional Statements

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

-----------
    🌲 Nested Conditions

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
else:
    print("Not a positive number")

    🧠 What I Understood Clearly
-- Strings are just sequences — slicing and indexing is super useful.

-- Conditional statements give programs logic and decision-making power.

-- String functions help manipulate text efficiently.
   

❓ Doubts or Confusions :

🔸 Slightly confused about slicing with negative indexes — will revise tomorrow.