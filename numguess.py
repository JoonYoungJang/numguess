from random import randint


# Create answer range: 1 to 100 (integer)
answer = randint(1, 100)

# print debugging
# print(answer)

# Get User's name, guess

user_name = input('Hello, there! What is your name? ')
guess = int(input(f'Hi, {user_name}. Guess the number(1-100): '))

# print to check
print(user_name, guess)

# Check and print correct or not
if guess == answer:
    print('Congrats!')
else:
    print(f'You are wrong! The answer is {answer})
