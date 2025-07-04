# 📘 Day 4 Basics – Lists & Tuples in Python

---

## 🔹 1. Lists in Python

A **list** is an ordered, changeable (mutable) collection of items.

```python
fruits = ["apple", "banana", "mango"]

Elements can be of any data type

Duplicates are allowed

Indexing starts at 0

✅ Common List Operations: 
Operation	          Syntax/Example	           Result
Access element	   fruits[0]	                    'apple'
Change element	fruits[1] = "orange" Replaces"banana"with"orange"
Add element (end)	fruits.append("grape")	   Adds "grape"
Insert at index	fruits.insert(1, "kiwi")  Adds "kiwi" at position 1
Remove element	  fruits.remove("apple")   	Deletes "apple"
Delete by index	   del fruits[2]	        Deletes 3rd element
Clear all elements	 fruits.clear()	        Empties the list
Get length	          len(fruits)           Number of items

🔁 Looping through a List :
for fruit in fruits:
    print(fruit)


🔃 List Methods:

numbers = [5, 3, 8, 1]

numbers.sort()      # [1, 3, 5, 8]
numbers.reverse()   # [8, 5, 3, 1]
print(len(numbers)) # 4
print(max(numbers)) # 8
print(min(numbers)) # 1
print(sum(numbers)) # 17

🔹 2. List Slicing:

fruits = ["apple", "banana", "mango", "grape"]

print(fruits[1:3])   # ['banana', 'mango']
print(fruits[:2])    # ['apple', 'banana']
print(fruits[::2])   # ['apple', 'mango']

🔹 3. Tuples in Python:
A tuple is an ordered, unchangeable (immutable) collection.

dimensions = (100, 200, 300)
Defined using () instead of []

Cannot modify items after creation

Faster and safer for fixed data

✅ Tuple Operations:

Operation	            Example                    	Result
Access item	          dimensions[0]	                    100
Length	              len(dimensions)                    3
Count elements	     dimensions.count(100)	             1
Find index	         dimensions.index(200)	              1

❗ Tuples Are Immutable

dim = (10, 20)
# dim[0] = 30  ❌ This will raise an error!

🔁 Looping through Tuples: 
python
Copy
Edit
colors = ("red", "green", "blue")

for color in colors:
    print(color)

🔄 Tuple Slicing:
Same as list slicing:

nums = (10, 20, 30, 40, 50)

print(nums[1:4])  # (20, 30, 40)

🔍 Lists vs Tuples – Summary:

Feature	         List	                            Tuple
Brackets	     []	                                ()
Mutability	Mutable (can change items)	Immutable (cannot change)
Performance	   Slightly slower	                      Faster
Use Case	   Dynamic data	                 Fixed/static data

📌 Summary
Lists are perfect for dynamic collections (add/remove/modify).

Tuples are ideal for fixed data that shouldn't change.

Both support indexing, slicing, and looping.

Lists are mutable, tuples are immutable.

