# 1. Print a welcoming message
print("--- Welcome to our Program ---")

# 2. Take String input from the user
user_name = input("Enter your name: ")

# 3. Take Integer input (we convert it using int() because input() reads text)
user_age = int(input("Enter your age: "))

# 4. Calculate the birth year (Current Year is 2026)
birth_year = 2026 - user_age

# 5. Print the final results
print("Hello, " + user_name + "!")
print("Based on your age, you were born around: " + str(birth_year))
