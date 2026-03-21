# =========================================
# QUIZ APPLICATION (FOUNDATION LEVEL)
# =========================================

# List of questions
questions = [
    "1. What is the capital of India?",
    "2. Which planet is known as the Red Planet?",
    "3. How many days are there in a week?",
    "4. Which animal is known as the King of the Jungle?",
    "5. What is 5 + 3?"
]

# Options for each question (stored as simple strings)
options = [
    "a) Delhi  b) Mumbai  c) Chennai  d) Kolkata",
    "a) Earth  b) Mars  c) Venus  d) Jupiter",
    "a) 5  b) 6  c) 7  d) 8",
    "a) Tiger  b) Elephant  c) Lion  d) Bear",
    "a) 6  b) 7  c) 8  d) 9"
]

# Correct answers
answers = ["a", "b", "c", "c", "c"]


# -----------------------------------------
# Function: Run the quiz
# -----------------------------------------
def start_quiz():
    score = 0

    print("\nStarting Quiz...\n")

    # Loop through all questions
    for i in range(len(questions)):

        print(questions[i])
        print(options[i])

        user_answer = input("Enter your answer (a/b/c/d): ").lower()

        if user_answer == answers[i]:
            print("Correct!\n")
            score = score + 1
        else:
            print("Wrong!\n")

    print("Quiz Completed!")
    print("Your Score:", score, "/", len(questions))


# =========================================
# MAIN PROGRAM LOOP
# =========================================
while True:

    print("\n===== QUIZ APPLICATION =====")
    print("1. Start Quiz")
    print("2. Exit")
    print("============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        start_quiz()

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")