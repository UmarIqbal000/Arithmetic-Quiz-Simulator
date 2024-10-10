import random
import operator

# Dictionary to map operator symbols to functions
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# Function to generate a random arithmetic problem
def generate_problem():
    num1 = random.randint(1, 20)  # Random number between 1 and 20
    num2 = random.randint(1, 20)  # Random number between 1 and 20
    operation = random.choice(list(operations.keys()))  # Randomly select an operator

    # Avoid division by zero
    if operation == '/' and num2 == 0:
        num2 = random.randint(1, 20)

    return num1, num2, operation

# Function to ask a quiz question
def ask_question(num1, num2, operation):
    print(f"What is {num1} {operation} {num2}?")
    correct_answer = round(operations[operation](num1, num2), 2)  # Round to 2 decimal places for division
    return correct_answer

# Main quiz game function
def quiz_game():
    score = 0
    total_questions = 5  # Number of questions in the quiz

    print("Welcome to the Fun Arithmetic Quiz Game!")
    print(f"You will be asked {total_questions} questions.")

    for i in range(total_questions):
        num1, num2, operation = generate_problem()
        correct_answer = ask_question(num1, num2, operation)

        # Get user's answer and validate it
        try:
            user_answer = float(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Oops! The correct answer was {correct_answer}.")

    # Display the final score
    print(f"Quiz over! Your final score is {score}/{total_questions}.")

# Run the quiz game
quiz_game()
