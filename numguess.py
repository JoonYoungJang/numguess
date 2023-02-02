from random import randint


# Create answer range: 1 to 100 (integer)
answer = randint(1, 100)

# Print answer (for debugging)
print(answer)

# Get User's name, guess

user_name = input('Hello, there! What is your name? ')
guess = input(f'Hi, {user_name}. Guess the number(1-100): ')

# print to check
print(user_name, guess)
