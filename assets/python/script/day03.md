# **Day 03 - Class Script**

## Table of Contents

1. [Warm-up & Recap](#warm-up--recap)
2. [Introducing Operators](#introducing-operators)
3. [Hands-On: Apple Operator Playground](#hands-on-apple-operator-playground)
4. [Decision Making in Python](#decision-making-in-python)
5. [Activity 1: Basic Apple Checker](#activity-1-basic-apple-checker)
6. [Activity 2: Health Checker](#activity-2-health-checker)
7. [Activity 3: Apple Type Classifier](#activity-3-apple-type-classifier)
8. [Activity 4: Shopping Decision Maker](#activity-4-shopping-decision-maker)
9. [Activity 5: Apple Ripeness Checker](#activity-5-apple-ripeness-checker)
10. [Review & Reflection](#review--reflection)
11. [Homework & Practice](#homework--practice)
12. [Next Steps](#next-steps)

---

## Warm-up & Recap

👩‍🏫 **Teacher Script:**

* “Yesterday we learned about **variables** and **formatted printing**. Can someone remind me how we stored the apple’s color in a variable?”
* (Wait for student responses)
* Transition: “Great! Today, let’s go one step ahead. Computers don’t just store values; they can **compare** them and make **decisions**. Just like us, computers also ask: *Is this red? Is this enough money?*”

---

## Introducing Operators

👩‍🏫 **Teacher Script:**

* “Operators are symbols that help us compare values.”
* Write on board: `==, !=, >, <, >=, <=`
* Real-world analogy: “Suppose an apple costs ₹50. If I have ₹60, can I buy it? → Yes, because ₹60 >= ₹50.”

---

## Hands-On: Apple Operator Playground

👩‍🏫 **Teacher Script:**
“Let’s try some quick tests in Python. Observe carefully: you will only get `True` or `False`.”

```python
# Equal to (==)
print("Is the apple red?", "red" == "red")

# Not equal (!=)
print("Is the apple not green?", "red" != "green")

# Greater than (>)
print("Is apple price greater than budget?", 60 > 50)

# Less than (<)
print("Is apple price less than budget?", 40 < 50)

# Greater than or equal (>=)
print("Do you have enough money?", 50 >= 50)

# Less than or equal (<=)
print("Is apple weight small?", 150 <= 200)
```

👉 **Student Task:** Run each line and read aloud whether it is `True` or `False`.
👉 **Discussion Prompt:** “Why do you think Python returned `True` for this one? Can someone explain?”

---

## Decision Making in Python

👩‍🏫 **Teacher Script:**

* “Now, let’s talk about **decision making**. Imagine you are at a fruit shop. If you see a red apple, you pick it. Otherwise, you don’t. That’s a decision.”
* “Python uses `if`, `elif`, and `else` to make decisions.”
* **Explain with flow:** *Condition → If True → Action → Else → Another Action.*
* “If there are multiple choices, Python checks one by one using `elif`. If there are no choices left, it does nothing.”

👉 **Interactive Question:** “In real life, where do we make such choices?” (Possible answers: choosing clothes, deciding lunch, exams pass/fail, etc.)

---

## Activity 1: Basic Apple Checker 🍎

```python
apple_color = "red"

if apple_color == "red":
    print("This is a red apple! 🍎")
else:
    print("This apple isn't red.")
```

👉 **Ask Students:** “What happens if I change `apple_color` to `green`?”
👉 Let one student try it out.

---

## Activity 2: Health Checker ❤️

```python
is_healthy = True

if is_healthy:
    print("This apple is good for you! 👍")
else:
    print("Maybe choose a different fruit. 👎")
```

👉 **Discussion Prompt:** “What if `is_healthy = False`? Can someone predict the output before running?”

---

## Activity 3: Apple Type Classifier 🔍

```python
apple_type = input("What color is the apple? ").lower()

if apple_type == "red":
    print("Classic red apple")
elif apple_type == "green":
    print("Tangy green apple")
elif apple_type == "yellow":
    print("Sweet golden apple")
else:
    print("Unknown apple variety")
```

👉 **Student Interaction:** Each student types a color and sees the classification.
👉 **Challenge Question:** “What happens if I type `BLUE` in uppercase?”

---

## Activity 4: Shopping Decision Maker 🛒

```python
budget = int(input("What is your budget? "))
apple_price = int(input("What is the apple price? "))

if budget >= apple_price:
    print("You can buy the apple! 🛍️")
else:
    print("You don’t have enough money. 💸")
```

👉 **Teacher Prompt:** “If I have ₹50 and the apple costs ₹60, can I buy it? Let’s test.”
👉 **Follow-up:** “What if both are equal? (budget = 50, apple\_price = 50)”

---

## Activity 5: Apple Ripeness Checker 🟢🔴

```python
color = input("Apple color (green / red): ")

if color.lower() == "green":
    print("Not ready yet, wait! ⏳")
elif color.lower() == "red":
    print("Ripe and ready to eat! 🍎")
else:
    print("I don’t know this color. ❓")
```

👉 **Interactive Question:** “What if someone types ‘yellow’? Why does the program give ❓?”
👉 **Link Back:** “This is where multiple `elif` conditions are useful.”

---

## Review & Reflection

👩‍🏫 **Teacher Script:**
“Let’s summarize. Who can tell me…”

1. “Which operators we learned today?”
2. “How do we use `if-else` in real life?”
3. “What happens if none of the conditions are true?”

👉 Encourage peer explanation: One student answers, another student adds to it.

---

## Next Steps

👩‍🏫 **Teacher Script:**
“Tomorrow (Day 04), we’ll go deeper into **elif chains** and learn about **nested if statements**. We’ll also create real-world examples like grading system and ticket price checker.”

---
