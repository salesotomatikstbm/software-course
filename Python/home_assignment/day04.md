![alt text](otomatiks.jpg)
---

# **Day - 04 - Home Assignment: Vinayagar Chaturthi Special**

---

## **Question: Vinayagar Chaturthi Prasadam Counter**

### **Objective:**

To calculate the total prasadam (modaks and bananas), check if the quantity is sufficient for all the guests, and display the prasadam details with Vinayagar Chaturthi greetings.
---

### **What You Need to Do:**

1. **Step 1: Get Guest and Prasadam Details**

   * Ask the user:

     * How many guests are coming?
     * How many modaks you prepared?
     * How many bananas you prepared?

   *Hint:* Use `input()` and `int()` to store these values in variables.

   ```python
   guests = int(input("How many guests are coming? "))
   modaks = int(input("How many modaks do you have? "))
   bananas = int(input("How many bananas do you have? "))
   ```

---

2. **Step 2: Calculate Total Prasadam**

   * Add modaks and bananas together.
   * Print the total prasadam items.

   *Hint:* `total_prasadam = modaks + bananas`

---

3. **Step 3: Check If Enough for All Guests**

   * Each guest should get **1 modak and 1 banana**.
   * So total prasadam needed = `guests * 2`
   * Print prasadam needed.
   * Use **if-else** to compare total prasadam with needed prasadam.

   ```python
   needed = guests * 2
   ```

---

4. **Step 4: Extra Check**

   * If total prasadam is more than 50 → print a special message.

---

<!-- ### **Python Code Example:**

```python
# Vinayagar Chaturthi Prasadam Counter

# Step 1: Get inputs
guests = int(input("How many guests are coming? "))
modaks = int(input("How many modaks do you have? "))
bananas = int(input("How many bananas do you have? "))

# Step 2: Calculate total prasadam
total_prasadam = modaks + bananas
print("Total prasadam items:", total_prasadam)

# Step 3: Check prasadam needed
needed = guests * 2
print("Total prasadam needed:", needed)

if total_prasadam >= needed:
    print("Enough prasadam for everyone!")
else:
    print("Not enough prasadam, please prepare more.")

# Step 4: Extra Check
if total_prasadam > 50:
    print("Wow! You have a grand prasadam feast for Vinayagar Chaturthi!")
```

--- -->

### **Example Run:**

**Inputs:**

```
How many guests are coming? 20
How many modaks do you have? 25
How many bananas do you have? 30
```

**Output:**

```
Total prasadam items: 55
Total prasadam needed: 40
Enough prasadam for everyone!
Wow! You have a grand prasadam feast for Vinayagar Chaturthi!
```

---

