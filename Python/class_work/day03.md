**Day - 03 - Class Flow** :

**Apple Operator Playground** 🍎:

---


```python
# Equal to (==)
print("Is the apple red?", "red" == "red")   # True

# Not equal (!=)
print("Is the apple not green?", "red" != "green")   # True

# Greater than (>)
print("Is apple price greater than budget?", 60 > 50)   # True

# Less than (<)
print("Is apple price less than budget?", 40 < 50)   # True

# Greater than or equal (>=)
print("Do you have enough money?", 50 >= 50)   # True

# Less than or equal (<=)
print("Is apple weight small?", 150 <= 200)   # True

```

---


# **Apple Decision Maker: Using If-Else Statements**

We will learn how computers **make decisions** using `if`, `elif`, and `else`.

---

## **1. Basic Apple Checker** 🍎

```python
apple_color = "red"

if apple_color == "red":
    print("This is a red apple! 🍎")
else:
    print("This apple isn't red.")
```

👉 If the apple is red → print “red apple”.
👉 Otherwise → print “not red”.

---

## **2. Health Checker** ❤️

```python
is_healthy = True

if is_healthy:
    print("This apple is good for you! 👍")
else:
    print("Maybe choose a different fruit. 👎")
```

👉 If healthy → say good.
👉 Otherwise → say bad.

---

## **3. Apple Type Classifier** 🔍

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

👉 Type the color → computer tells you the type.

---

## **4. Shopping Decision Maker (Corrected)** 🛒

```python
budget = int(input("What is your budget? "))
apple_price = int(input("What is the apple price? "))

if budget >= apple_price:
    print("You can buy the apple! 🛍️")
else:
    print("You don’t have enough money. 💸")
```

**Step-by-step thinking:**

1. Ask how much money you have (`budget`).
2. Ask the price of the apple (`apple_price`).
3. If budget ≥ price → you can buy.
4. Otherwise → not enough money.

---

## **5. Apple Ripeness Checker (Simplified)** 🟢🔴

```python
color = input("Apple color (green / red): ")

if color.lower() == "green":
    print("Not ready yet, wait! ⏳")
elif color.lower() == "red":
    print("Ripe and ready to eat! 🍎")
else:
    print("I don’t know this color. ❓")
```

**Step-by-step thinking:**

1. Ask for apple color.
2. If it’s green → not ready.
3. If it’s red → ready to eat.
4. If it’s something else → unknown.

---

