# Python Practice Questions

This repository contains beginner-friendly Python programming exercises and solutions covering:

* Strings
* Lists
* Dictionaries
* Tuples
* Sets

These exercises are useful for practicing Python basics, data structures, loops, functions, and problem-solving skills.

---

# Topics Covered

## String Questions

* Get first three characters of a string
* Caesar cipher encryption
* Remove duplicate characters
* Delete occurrences of a character
* Count leap years in a range
* Insert spaces before capital letters

---

## List Questions

* Generate square numbers
* Difference between lists
* Concatenate list with range
* Convert list to dictionary
* Move zeros to the end
* Round and process numbers
* Count lists inside a list

---

## Dictionary Questions

* Concatenate dictionaries
* Print distinct dictionary values
* Combine dictionaries using Counter
* Find top items in a shop
* Filter dictionary by values
* Extract values from list of dictionaries

---

## Tuple Questions

* Replace tuple values
* Remove empty tuples
* Sort tuples by float values
* Convert tuple to integer
* Sum tuple elements
* Calculate tuple averages

---

## Set Questions

* Find set length
* Add members to a set
* Remove items from a set
* Create set intersection
* Create set union
* Create set difference
* Find maximum and minimum values

---

# Project Structure

```bash
python-practice/
│
├── strings.py
├── lists.py
├── dictionaries.py
├── tuples.py
├── sets.py
└── README.md
```

---

# Requirements

* Python 3.14.5

---

# How to Run

1. Clone the repository

```bash
git clone 
```

2. Open the project folder

```bash
cd python-practice
```

3. Run a Python file

```bash
python strings.py
```

OR

```bash
python lists.py
```

---

# Sample Exercises

## Example 1: Caesar Cipher

```python
def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

print(caesar_cipher("Python", 3))
```

---

## Example 2: Move Zeros to End

```python
numbers = [1, 0, 2, 0, 3, 0]

result = [x for x in numbers if x != 0]
result += [0] * numbers.count(0)

print(result)
```

---

# Learning Objectives

This project helps learners practice:

* Python syntax
* Functions
* Loops
* Conditionals
* List comprehensions
* Dictionaries
* Tuples
* Sets
* String manipulation
* Problem-solving techniques

---


# AUTHORS

* BRIAN EDWARD NGOYONI
* COLLINS KOOME
* MITCHELLE WANJUGU


---

# License

This project is open-source and available for anyone who wants to revise
