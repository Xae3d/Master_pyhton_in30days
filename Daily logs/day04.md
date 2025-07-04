# 🐍 Day 4 – Lists & Tuples in Python

📅 **Date:** June 8, 2025  
🕒 **Status:** Completed ✅  
🧠 **Mood:** Excited and getting more confident! 🧠🔥

---

## ✅ What I Learned Today

Today I explored two important Python data structures:

1. 🔹 **Lists** – Ordered, changeable (mutable) collections
2. 🔹 **Tuples** – Ordered, unchangeable (immutable) collections

---

## 📘 Notes Summary

📌 Check detailed notes here → [notes/day04basics.md](../notes/day04basics.md)

---

## 🧪 Code Snippets

### 📚 Working with Lists:

fruits = ["apple", "banana", "mango"]

print(fruits[0])        # apple
fruits.append("grape")  # add at end
fruits.remove("banana") # remove item
print(fruits)

fruits[1] = "orange"    # modify item
print(fruits)

📚 List Functions & Methods

numbers = [4, 2, 9, 1]

numbers.sort()
print(numbers)      # [1, 2, 4, 9]

numbers.reverse()
print(numbers)      # [9, 4, 2, 1]

print(len(numbers)) # 4
print(sum(numbers)) # 16

📚 Working with Tuples

dimensions = (100, 200)
print(dimensions[0])   # 100

# dimensions[0] = 300  # ❌ Error: tuples are immutable


🔁 Looping through Lists & Tuples

fruits = ["apple", "mango", "grape"]

for fruit in fruits:
    print(fruit)

nums = (10, 20, 30)
for n in nums:
    print(n)

   
🧠 What I Understood Clearly
Lists are mutable → I can add, remove, or modify elements.

Tuples are immutable → Fixed once created.

Indexing and looping works similarly in both.

❓ Doubts or Confusions
🔸 Need to explore slicing more with tuples (especially in nested structures).

📍 Next Up:
- Day 5 → Dictionaries: Creating, accessing, modifying key-value pairs.

---
