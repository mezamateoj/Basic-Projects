#rock, paper, scissors
import random
from enum import IntEnum

# comparissons
class Action(IntEnum):
    rock = 0
    paper = 1
    scissors = 2

# user selection
def user():
    choices = [f'{action.name}[{action.value}]' for action in Action]
    join_choices = ' '.join(choices)
    user = int(input(f'Choose a number for {join_choices}: '))
    action = Action(user)
    return action

# computer selection
def computer_action():
    choice = random.randint(0, len(Action) - 1)
    action = Action(choice)
    return action


# winner function
def winner(user, computer_action):
    if user == computer_action:
        print(f'You both chose {user.name}, it\'s a tie')
    elif user == Action.rock:
        if computer_action == Action.scissors:
            print('You win, computer chose scissors')
        else:
            print('Paper just made you lose')
    elif user == Action.paper:
        if computer_action == Action.rock:
            print('You win, lucky the computer chose rock')
        else:
            print('Loser, to bad the computer chose scissors')
    elif user == Action.scissors:
        if computer_action == Action.paper:
            print('win, the computer chose paper')
        else:
            print('Loser, the computer chose rock')


# game flow
while True:
    try:
        user_selection = user()
    except ValueError as error:  # in case player chose 3 or more
        str_range = f'[0, {len(Action) - 1}]'
        print(f'Please, select a number between {str_range}')
        continue

    compu = computer_action()
    winner(user_selection, compu)

    again = input('Play one more time? y/n:')
    if again.lower() != 'y':
        break







