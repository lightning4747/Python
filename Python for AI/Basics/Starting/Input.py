# Get input from the user. input() always returns a string.
user_name = input("What is your name? ")
user_age = input("How old are you? ")

# We need to convert the age string to an integer to do math.
user_age_int = int(user_age)
birth_year = 2024 - user_age_int

# Print a personalized message.
print(f"Wow {user_name}! You were born around {birth_year}.")
#Mini-Project: Write a program that asks for a temperature in Fahrenheit and converts it to Celsius. The formula is: Celsius = (Fahrenheit - 32) * 5/9