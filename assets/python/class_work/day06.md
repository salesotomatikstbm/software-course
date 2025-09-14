---

### **Day 06 - Class Flow: Lists, Tuples, Sets, and Dictionaries**

---

### **1. Lists** (A list is a collection of items)

```python
# Create a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Access an item
print(fruits[1])  # Output: banana (lists start from 0)

# Modify an item
fruits[0] = "kiwi"
print(fruits)  # Output: ['kiwi', 'banana', 'cherry']

# Add an item
fruits.append("orange")
print(fruits)  # Output: ['kiwi', 'banana', 'cherry', 'orange']

# Remove an item
fruits.remove("banana")
print(fruits)  # Output: ['kiwi', 'cherry', 'orange']
```

* **Lists** can store many items. You can add, change, and remove items easily.

---

### **2. Tuples** (A tuple is like a list, but you cannot change it)

```python
# Create a tuple
coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

# Access an item
print(coordinates[0])  # Output: 10

# You cannot change a tuple
# coordinates[0] = 50  # This will give an error because tuples cannot be changed
```

* **Tuples** are similar to lists, but once created, their values cannot be changed.

---

### **3. Sets** (A set is a collection of unique items)

```python
# Create a set
fruits_set = {"apple", "banana", "cherry"}
print(fruits_set)  # Output: {'banana', 'apple', 'cherry'}

# Add an item
fruits_set.add("orange")
print(fruits_set)  # Output: {'banana', 'apple', 'cherry', 'orange'}

# Remove an item
fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple', 'cherry', 'orange'}
```

* **Sets** store unique items. They automatically remove duplicates and do not care about the order of the items.

---

### **4. Dictionaries** (A dictionary stores data in key-value pairs)

```python
# Create a dictionary
person = {"name": "Arun", "age": 27}
print(person)  # Output: {'name': 'Arun', 'age': 27}

# Access a value using its key
print(person["name"])  # Output: Arun

# Change a value
person["age"] = 29
print(person)  # Output: {'name': 'Arun', 'age': 29}

# Add a new key-value pair
person["city"] = "Kallakurichi"
print(person)  # Output: {'name': 'Arun', 'age': 29, 'city': 'Kallakurichi'}
```

* **Dictionaries** store data as **key-value pairs**, where each key has a value. You can easily look up values using keys.

---

### **Recap for Kids**

* **Lists**: Think of it as a list of items you can change anytime.
* **Tuples**: Like lists, but once you create them, they can't be changed.
* **Sets**: A collection that doesn’t allow duplicate items. It doesn’t care about the order.
* **Dictionaries**: A collection where you use keys to find the values. It's like a small address book.

---
