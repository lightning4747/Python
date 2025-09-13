print("Welcome to the Python Quiz!")
print("Answer the following questions:")

# Ask questions and get answers
answer1 = input("What is the capital of France? ")
answer2 = input("What is 2 + 2? ")
answer3 = input("What is the keyword for creating a function in Python? ")

# Check the answers and calculate a score
score = 0
if answer1.lower() == "paris": # Using .lower() so "Paris" or "paris" is correct
    score += 1
if answer2 == "4":
    score += 1
if answer3.lower() == "def":
    score += 1

# Give the result
print(f"\nQuiz Over! Your final score is: {score}/3")