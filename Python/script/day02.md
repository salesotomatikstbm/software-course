# **Day 02 - Class Script (Fruit Shop Conversation)**

## Table of Contents

1. [Warm-up & Fruit Shop Role-Play](#warm-up--fruit-shop-role-play)
2. [Introducing Variables with Apple Brochure](#introducing-variables-with-apple-brochure)
3. [Variables & Data Types](#variables--data-types)
4. [Checking Data Types](#checking-data-types)
5. [f-Strings for Output Formatting](#f-strings-for-output-formatting)
6. [Activity 1: Create Apple Brochure in Python](#activity-1-create-apple-brochure-in-python)
7. [Activity 2: Data Type Explorer](#activity-2-data-type-explorer)
8. [Activity 3: Print Brochure with f-Strings](#activity-3-print-brochure-with-f-strings)
9. [Review & Reflection](#review--reflection)
10. [Homework & Practice](#homework--practice)
11. [Next Steps](#next-steps)

---

## Warm-up & Fruit Shop Role-Play

👩‍🏫 **Teacher Script:**
“Before we write code, let’s imagine we are in a **fruit shop**. One student will be the **seller**, another will be the **buyer**.”

👉 **Role-Play Example:**

* **Seller:** “Hello! Today we have fresh apples.”
* **Buyer:** “Great! What is the color of the apple?”
* **Seller:** “They are red.”
* **Buyer:** “How much do they cost per kg?”
* **Seller:** “₹120.5 per kg.”
* **Buyer:** “I’ll take 6 kg. Are these apples healthy?”
* **Seller:** “Yes! Very healthy.”

👩‍🏫 **Teacher Connect:**
“Did you notice the key details in this conversation?

* Fruit name → apple
* Fruit color → red
* Quantity → 6 kg
* Price → 120.5 rupees
* Healthy → True

In Python, we can **store all this information in variables**, just like the shopkeeper keeps a record.”

---

## Introducing Variables with Apple Brochure

👉 **Code Example:**

```python
fruit_name = "apple"
fruit_color = "red"
quantity_kg = 6
price_rupees = 120.5
healthy = True
```

👩‍🏫 **Ask Students:**

* “What value is stored in `fruit_name`?”
* “Which variable represents the quantity?”

---

## Variables & Data Types

👩‍🏫 **Teacher Script:**
“These variables belong to different **data types**. Let’s see.”

| Example values                            | Data type |
| ----------------------------------------- | --------- |
| `"apple"`, `"red"`, `"my name is ramesh"` | `str`     |
| `12`, `18000`, `-250`                     | `int`     |
| `120.5`, `3.14`, `-0.5`                   | `float`   |
| `True`, `False`                           | `bool`    |

👉 **Prompt:** “Which type is best for the word *red*? What about the price?”

---

## Checking Data Types

👉 **Code Example:**

```python
print(type(fruit_name))
print(type(fruit_color))
print(type(quantity_kg))
print(type(price_rupees))
print(type(healthy))
```

👩‍🏫 **Interactive Question:** “Predict first — what do you think `price_rupees` will show? `int` or `float`?”

---

## f-Strings for Output Formatting

👉 **Code Example:**

```python
print(f"Fruit name is {fruit_name}")
print(f"Fruit color is {fruit_color}")
print(f"Quantity in kg is {quantity_kg}")
print(f"Price in rupees is {price_rupees}")
print(f"Is it healthy? {healthy}")
```

👩‍🏫 **Teacher Prompt:**
“See how clean this looks! If I remove the `f`, what do you think will happen?”

---

## Activity 1: Create Apple Brochure in Python 🍎

* Students recreate the **apple brochure** in Python.
* Ask them to change:

  * fruit\_color → `"green"`
  * quantity\_kg → `10`
  * healthy → `False`

---

## Activity 2: Data Type Explorer 🔍

👉 **Code Example:**

```python
x = "120.5"
y = 120.5

print(type(x))
print(type(y))
```

👩‍🏫 **Ask Students:**

* “Why is `"120.5"` a string but `120.5` is a float?”

---

## Activity 3: Print Brochure with f-Strings 📝

👉 **Code Example:**

```python
print(f"{fruit_name.upper()} BROCHURE")
print(f"Color: {fruit_color}")
print(f"Quantity: {quantity_kg} kg")
print(f"Price: ₹{price_rupees}")
print(f"Healthy Choice: {healthy}")
```

👩‍🏫 **Extension Prompt:**
“Try making the brochure for another fruit, like mango or orange.”

---

## Review & Reflection

👩‍🏫 **Teacher Script:**
“Let’s review today’s key ideas. Who can tell me…”

1. “What is a variable?”
2. “What are the 4 data types we used?”
3. “What does `type()` do?”
4. “How do f-strings help us?”

---



## Next Steps

👩‍🏫 **Teacher Script:**
“Tomorrow (Day 03), we’ll move from **storing values** to **comparing values** using operators, and make decisions with `if-else`. For example: *Can you afford to buy the apple with your budget?*”

---
