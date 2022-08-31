import random
logo = ''' _______  __   __  _______  _______  _______    _______  __   __  _______    __    _  __   __  __   __  _______  _______  ______
|       ||  | |  ||       ||       ||       |  |       ||  | |  ||       |  |  |  | ||  | |  ||  |_|  ||  _    ||       ||    _ |
|    ___||  | |  ||    ___||  _____||  _____|  |_     _||  |_|  ||    ___|  |   |_| ||  | |  ||       || |_|   ||    ___||   | ||
|   | __ |  |_|  ||   |___ | |_____ | |_____     |   |  |       ||   |___   |       ||  |_|  ||       ||       ||   |___ |   |_||_
|   ||  ||       ||    ___||_____  ||_____  |    |   |  |       ||    ___|  |  _    ||       ||       ||  _   | |    ___||    __  |
|   |_| ||       ||   |___  _____| | _____| |    |   |  |   _   ||   |___   | | |   ||       || ||_|| || |_|   ||   |___ |   |  | |
|_______||_______||_______||_______||_______|    |___|  |__| |__||_______|  |_|  |__||_______||_|   |_||_______||_______||___|  |_|'''
attempts_left = 0
print(logo)
print('Welcome to the Number Guessing Game! You will need to guess secret number from 1 to 100')
difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    attempts_left = 10
elif difficulty == 'hard':
    attempts_left = 5
else:
    print('There is no such difficulty level... Sorry!')
    quit()

secret_number = random.randint(1,101)

users_guess = 0

while users_guess != secret_number:
    users_guess = int(input(f"""You have {attempts_left} attempts remaining to guess the number
Make a guess: """))
    if users_guess > secret_number:
        print('Too High!')
        attempts_left -= 1
    elif users_guess < secret_number:
        print('Too low!')
        attempts_left -= 1
    if attempts_left == 0:
        break

if attempts_left > 0:
    print('Congrats, you won! :)')
else:
    print('You loose... Yet again :/')
