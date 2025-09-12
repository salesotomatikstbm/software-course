# **Day - 04 - Class Flow**

---

## **Question 01: School Supplies Adventure**

### **Objective:**

Organize your school supplies and practice simple math in Python.

---

### **Step 1: Count Your Supplies**

1. **How many notebooks do you have?**
   *Hint:* Use `input()` and `int()`.

2. **How many pens do you have?**
   *Hint:* Same as above.

---

### **Step 2: Do Some Math**

1. **Find the total items you have.**
   *Hint:* Use `+` operator.

2. **Check if you have more notebooks than pens.**
   *Hint:* Use `if notebooks > pens:`

3. **Check if notebooks are more than twice the pens.**
   *Hint:* Use `if notebooks > 2 * pens:`

---

### **Step 3: Extra Simple Task** 

Print a short message like:

* `"Great job organizing your school supplies!"`

---

## **Question 02: Pocket Money Shopper**

### **Objective:**

Use your pocket money to check what school supplies you can buy.

---

### **Step 1: Enter the Money & Prices**

1. **How much money do you have?**
   *Hint:* Use `input()` and `int()`.

2. **How much does one notebook cost?**
   *Hint:* Same way as above.

3. **How much does one pen cost?**
   *Hint:* Same way as above.

---

### **Step 2: Shopping Questions**

1. **Can you afford at least 1 notebook?**
   *Hint:* Use `if money >= notebook_price:`

2. **Can you afford 5 notebooks?**
   *Hint:* Multiply price × 5.

3. **If you don’t have enough for even 1 notebook, print `"Save more money!"`**

---

### **Step 3: Extra Simple Task** 

Print a short message like:

* `"Shopping is fun when you plan your money!"`

---

## **Question 03: Big School Supplies Game**

### **Objective:**

Buy notebooks and pens together, and check if your pocket money is enough.

---

### **Python Code Example:**

```python
# Big School Supplies Game

notebook_price = int(input("Price of one notebook: "))
pen_price = int(input("Price of one pen: "))
money = int(input("How much pocket money do you have? "))

notebooks = int(input("How many notebooks do you want? "))
pens = int(input("How many pens do you want? "))

# Calculate total cost
total_cost = (notebook_price * notebooks) + (pen_price * pens)
print("Final Bill:", total_cost)

# Compare with money
if money > total_cost:
    print("You can pay! Money left:", money - total_cost)
elif money == total_cost:
    print("You spent all your money!")
else:
    print("Not enough money. You need more:", total_cost - money)
```

---

### **Full Output Example:**

**Inputs:**

```
Price of one notebook: 20  
Price of one pen: 5  
How much pocket money do you have? 100  
How many notebooks do you want? 3  
How many pens do you want? 4  
```

**Output:**

```
Price of one notebook: 20
Price of one pen: 5
How much pocket money do you have? 100
How many notebooks do you want? 3
How many pens do you want? 4

Final Bill: 80
You can pay! Money left: 20
```

---

