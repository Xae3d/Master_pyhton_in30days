# 📘 Day 5 Basics – Python Dictionaries

---

## 🔹 1. What is a Dictionary?

A **dictionary** in Python is a collection of **key-value pairs**, where:

- Keys are **unique** and usually strings
- Values can be of any data type
- Dictionaries are **unordered** (before Python 3.7), but insertion-ordered in newer versions

```python
person = {
    "name": "Saeed",
    "age": 21,
    "city": "Mumbai"
}

🔹 2. Creating a Dictionary:

student = {
    "name": "Saeed",
    "course": "Python",
    "year": 2025
}

You can also create an empty dictionary:

empty_dict = {}

🔹 3. Accessing Values:

print(student["name"])        # Saeed
print(student.get("course")) # Python

⚠️ .get() is safer:
If the key doesn’t exist:

print(student.get("marks", "Not found"))  # Output: Not found

🔹 4. Updating and Adding :

student["year"] = 2026               # Update
student["email"] = "saeed@email.com" # Add new key-value pair

🔹 5. Removing Items:

student.pop("course")     # Removes 'course' key
del student["year"]       # Deletes key 'year'
student.clear()           # Empties the dictionary

🔹 6. Dictionary Functions and Methods:
Method	                          Description
dict.keys()	                   Returns all keys
dict.values()	               Returns all values
dict.items()	          Returns all key-value pairs as tuples
dict.update()	           Updates one dictionary with another
dict.pop(key)	            Removes item with given key
dict.clear()	            Clears the entire dictionary

Example:
student = {
    "name": "Saeed",
    "age": 21
}

print(student.keys())    # dict_keys(['name', 'age'])
print(student.values())  # dict_values(['Saeed', 21])
print(student.items())   # dict_items([('name', 'Saeed'), ('age', 21)])

🔹 7. Looping Through Dictionaries


🔁 Loop over keys:
for key in student:
    print(key, student[key])


🔁 Loop over keys and values:

for key, value in student.items():
    print(f"{key} → {value}")


🔹 8. Dictionary Nesting (Advanced)
You can store dictionaries inside other dictionaries:

students = {
    "student1": {"name": "Saeed", "age": 21},
    "student2": {"name": "Shravani", "age": 22}
}

print(students["student1"]["name"])  # Saeed

🔍 Dictionaries vs Lists:

Feature         	  Dictionary	                  List
Structure	  Key-value pairs	                 Indexed elements
Lookup Time	   Faster with keys	               Slower with search
Ordered	Yes    (in Python 3.7+)	                    Yes
Use Case	  Structured, labeled data	      Ordered collections

📌 Summary

-- Dictionaries are great for mapping labels to values

-- Easy to add, update, and remove data

-- Use .get() for safe access

-- Loop through using .items() for keys + values

-- Support nesting and are highly flexible

