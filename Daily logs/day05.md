# 🐍 Day 5 – Python Dictionaries

📅 **Date:** June 9, 2025  
🕒 **Status:** Completed ✅  
🧠 **Mood:** Feeling smart and structured! 🧩🔑

---

## ✅ What I Learned Today

Today I explored one of Python’s most powerful data structures:

1. 🔹 **Dictionaries** – Storing data in key-value pairs
2. 🔹 Accessing and updating values
3. 🔹 Using built-in dictionary methods
4. 🔹 Looping through dictionaries

---

## 📘 Notes Summary

📌 Detailed notes here → [notes/day05basics.md](../notes/day05basics.md)

---

## 🧪 Code Snippets

### 📚 Creating a Dictionary

```python
student = {
    "name": "Saeed",
    "age": 21,
    "course": "Python"
}

print(student["name"])   # Saeed
print(student.get("age")) # 21

🔄 Updating & Adding Values :

student["age"] = 22           # Update value
student["city"] = "Mumbai"    # Add new key-value pair

print(student)

❌ Removing Items:

student.pop("course")         # Removes 'course'
del student["age"]            # Deletes 'age'
student.clear()               # Empties dictionary

🔁 Looping Through a Dictionary :

for key in student:
    print(key, ":", student[key])

# OR

for key, value in student.items():
    print(f"{key} → {value}")


🧠 What I Understood Clearly
Dictionaries store data with unique keys

We can easily add, update, or delete items

.get(), .keys(), .values() are useful methods

Looping through items() gives both key & value

❓ Doubts or Confusions
🔸 None today! Dictionaries feel very intuitive and useful.

