# **Day - 05 - Class Flow**

### 1. Calculator

```python
a = 10
b = 5
operation = input("Choose operation (+, -, *, /): ")

match operation:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        print("Result:", a / b)
    case _:
        print("Invalid operation")
```

---

### 2. Grade Evaluator

```python
grade = input("Enter grade (A, B, C, D, F): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case "D":
        print("Poor")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")
```

---

### 3. Month Name Finder

```python
month = int(input("Enter month number (1-12): "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number")
```

---

### 4. Simple Login Role Checker

```python
role = input("Enter role (admin, user, guest): ").lower()

match role:
    case "admin":
        print("You have full access")
    case "user":
        print("You have limited access")
    case "guest":
        print("You have view-only access")
    case _:
        print("Unknown role")
```

---

### 5. Weather Response

```python
weather = input("Enter weather (sunny, rainy, cloudy, snowy): ").lower()

match weather:
    case "sunny":
        print("Wear sunglasses")
    case "rainy":
        print("Take an umbrella")
    case "cloudy":
        print("It might rain later")
    case "snowy":
        print("Wear warm clothes")
    case _:
        print("Unknown weather condition")
```

---
