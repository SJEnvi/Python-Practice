from game_data import data
import random
from art import logo, vs
from replit import clear

score = 0

def format_data(account):
  account_name = account['name']
  account_descr = account['description']
  account_country = account['country']
  return f'{account_name}, a {account_descr}, from {account_country}'

def check_answer(compare_a, compare_b, answer):
    if compare_a['follower_count'] > compare_b['follower_count']:
        correct_answer = 'a'
    else:
        correct_answer = 'b'

    if answer == correct_answer:
        global score
        score += 1
        print(f'You are correct :) Your current score is: {score}')
        return True
    else:
        print('Nope... :/')
        return False

def comparing(data):
    is_answer_correct = True
    for i in range(len(data)-1):
        if is_answer_correct == True:
            print(logo)
            compare_a = data[i]
            compare_b = data[i+1]
            print(f'Compare A: {format_data(compare_a)}')
            print(vs)
            print(f'Against B: {format_data(compare_b)}')
            answer = input("Who has more followers? Type 'A' or 'B'").lower()
            clear()
            is_answer_correct = check_answer(compare_a, compare_b, answer)
    return is_answer_correct

def game():
    random.shuffle(data)
    continue_game = comparing(data)
    if continue_game == False:
        print(f'You lost, your score is {score}')
    else:
        print(f'Congrats, you made it to the end! Your score is {score}')
    input("Press any key to close the app")
game()
