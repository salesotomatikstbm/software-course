# Assignment 01: Extending Fruit Description with Variables

We have already created variables for `fruit_name`, `fruit_color`, `quantity_kg`, `price_rupees`, and `healthy`.  
Now, extend this example by adding more variables to describe the fruit in greater detail.  
You can use different data types (`string`, `number`, `decimal`, `boolean`) and be as creative as you like.

## Think About:

### 1. Extra Details About the Fruit  
   - Size (e.g., `fruit_size = "medium"`)  
   - Origin (e.g., `origin_country = "India"`)  
   - Season (e.g., `best_season = "summer"`)  
   - Taste (e.g., `taste_profile = "sweet and tangy"`)  
   - Smell (e.g., `aroma = "fragrant"`)  

### 2. Nutritional Information  
   - Vitamins (e.g., `vitamin_c_mg = 28.5`)  
   - Calories (e.g., `calories_per_100g = 52`)  
   - Sugar content (e.g., `sugar_g = 12.2`)  
   - Fiber content (e.g., `fiber_g = 2.4`)  

### 3. Other Fun Facts  
   - Is it rare? (e.g., `is_rare = false`)  
   - Popularity (e.g., `popularity_rating = 9.5`)  
   - Used in festivals? (e.g., `used_in_festivals = true`)  

### 4. Your Own Ideas — Surprise Me!  
   - Add unique variables like:  
     - `days_since_harvest = 3`  
     - `organic_certified = true`  
     - `allergy_warning = "None"`  

Be creative and make your fruit description as detailed and interesting as possible!

---

# Assignment 02: Printing Fruit Descriptions Using Formatted Strings

Now that you've created detailed variables describing a fruit, it's time to display them in a structured and readable way using **formatted strings** (f-strings in Python).  

## Task:  
Write a program that prints a well-organized description of your fruit using all the variables you created earlier.  
Use **f-strings** (or your language's equivalent) to neatly combine text and variables in the output.

### Requirements:  
1. **Header Section**  
   - Start with a title (e.g., `"Ultimate Fruit Fact Sheet!"`).  
   - Include the fruit's name prominently.  

2. **Basic Details**  
   - Display the fruit's color, size, origin, and season.  
   - Example:  
     ```python
     print(f"Color: {fruit_color}, Size: {fruit_size}, From: {origin_country}")
     ```

3. **Nutritional Information**  
   - List key nutritional facts (e.g., calories, vitamins) with units.  
   - Example:  
     ```python
     print(f"Vitamin C: {vitamin_c_mg}mg per 100g | Sugar: {sugar_g}g")
     ```

4. **Fun Facts Section**  
   - Add creative details like rarity, popularity, or festival use.  
   - Example:  
     ```python
     print(f"Popularity: {popularity_rating}/10")
     ```

5. **Formatting Tips**  
   - Use **newlines (`\n`)** to separate sections.  
   - Align text neatly (e.g., colons or tabs for consistency).  

### Example Output:  
```text
Ultimate Fruit Fact Sheet!
---------------------------------  
Basic Info:  
- Color: Golden yellow  
- Size: Medium  
- Origin: India  
- Best Season: Summer  

Nutrition (per 100g):  
- Calories: 60kcal | Sugar: 14g  
- Vitamin C: 36mg | Fiber: 1.6g  

Fun Facts:  
Sweet and tangy, perfect for summer!  

---------------------------------  
```

### Bonus Challenge:  

- Add a **"Did You Know?"** section with a surprising fact.

---

# **Assignment 03: Creating Variables and Formatting Strings in Python**  

**Objective:**  
Learn how to:  
1. Create variables to store different types of data (like name, age, hobby, etc.).  
2. Use **f-strings** (formatted strings) to combine variables into a meaningful message.  

---  

### **Task 1: Student Bio**  
Create a short biography of a student using variables and then format them into a message.  

#### **Example Code:**  
```python
# Step 1: Create variables
name = "Alex"
age = 12
grade = 7
favorite_subject = "Science"
hobby = "playing chess"

# Step 2: Create a formatted string message
bio = f"My name is {name}. I am {age} years old and in grade {grade}. My favorite subject is {favorite_subject}, and I love {hobby}."

# Step 3: Print both messages
print("My Bio:")
print(bio)

```

#### **Expected Output:**  
```
My Bio:
My name is Alex. I am 12 years old and in grade 7. My favorite subject is Science, and I love playing chess.

```

---  

### **Task 2: Fairy Tale Short Story**  
Create a short fairy tale using variables and then modify parts of the story.  

#### **Example Code:**  
```python
# Step 1: Create variables
character = "dragon"
place = "enchanted forest"
magic_item = "golden amulet"
action = "saved the kingdom"

# Step 2: Create a formatted story
story = f"Once upon a time, a brave {character} lived in the {place}. One day, it found a {magic_item} and {action}!"

# Step 3: Print both versions
print("My Story:")
print(story)

```

#### **Expected Output:**  
```
My Story:
Once upon a time, a brave dragon lived in the enchanted forest. One day, it found a golden amulet and saved the kingdom!
```

---  

### **Your Turn!**  
Now, try creating your own:  
1. A short student bio or a fairy tale using variables.  
2. Format them into a message using f-strings.  
 

**Bonus:**  
- Try adding more variables (like friends, favorite food, or a twist in the story).  
 

Have fun coding! 🚀
