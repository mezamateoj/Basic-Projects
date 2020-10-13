# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:20:12 2020

@author: Mateo M
"""


sw = 400
sm = 540
sbeans = 120
scups = 9
smoney = 550


water = 400
milk = 540
beans = 120
cups = 9
money = 550


    

def buy():
    print()
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    select = input()
    global water, milk, beans, cups, money, sw, sm, scups, smoney, sbeans
    if select == '1':
        if max(water, beans) >= max(sw, sbeans) and cups > 0:
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
            return 'I have enough resources, making you a coffee!\n\nWrite action (buy, fill, take, remaining, exit):'
        elif min(water, beans) < min(sw, sbeans) or cups < 0:
            return 'Sorry, not enough resources!\n\nWrite action (buy, fill, take, remaining, exit):'
    elif select == '2':
         if max(water, milk, beans) >= max(sw, sbeans, sm) and cups > 0:
             water -= 350
             milk -= 75
             beans -= 20
             cups -= 1
             money += 7
             return 'I have enough resources, making you a coffee!\n\nWrite action (buy, fill, take, remaining, exit):'
         elif min(water, milk, beans) < min(sw, sbeans) or cups < 0:
            return 'Sorry, not enough resources!\n\nWrite action (buy, fill, take, remaining, exit):'
    elif select == '3':
        if max(water, milk, beans) >= max(sw, sbeans, sm) and cups > 0:
            water -= 200
            milk -= 100
            beans -= 12
            cups -= 1
            money += 6
            return 'I have enough resources, making you a coffee!\n\nWrite action (buy, fill, take, remaining, exit):'
        elif min(water, milk, beans) < min(sw, sbeans) or cups < 0: 
            return 'Sorry, not enough resources!\n\nWrite action (buy, fill, take, remaining, exit):'
    elif select == 'back':
        return '\nWrite action (buy, fill, take, remaining, exit):'
        
        

def fill():
    global water, milk, beans, cups
    print('Write how many ml of water do you want to add:')
    plus_water = int(input())
    water += plus_water
    print('Write how many ml of milk do you want to add:')
    plus_milk = int(input())
    milk += plus_milk
    print('Write how many grams of coffee beans do you want to add:')
    plus_beans = int(input())
    beans += plus_beans
    print('Write how many disposable cups of coffee do you want to add:')
    plus_cups = int(input())
    cups += plus_cups
    return '\nWrite action (buy, fill, take, remaining, exit):'
    
def take():
    global money
    print()
    print('I gave you $' + str(money))
    money = 0
    return '\nWrite action (buy, fill, take, remaining, exit):'
    
   
    
def remaining():
     return f'The coffee machine has\n{water} of water\n{milk} of milk\n{beans} of coffee beans\n{cups} of disposable cups\n${money} of money'
    
print('Write action (buy, fill, take, remaining, exit):')
action = input()

while True:
    if action == 'buy':
        print(buy())
        action = input()
    elif action == 'fill':
        print()
        print(fill())
        action = input()
    elif action == 'take':
        print(take())
        action = input()
    elif action == 'remaining':
        print()
        print(remaining())
        print()
        print('Write action (buy, fill, take, remaining, exit):')
        action = input()
    elif action == 'exit':
        break
 
    


 
    

