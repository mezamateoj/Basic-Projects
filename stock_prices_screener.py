# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import pandas_datareader as pdr
from time import sleep


symbols = 'AAPL GME SPY NFLX BB TSLA QQQ'.split()

options = ' Track Default lists, Show Default Lists, Add to Default, \
Edit Default List, Add new List, Quit'.split(',')



def show_default(symbols):
    symbols.sort()
    for i in symbols:
        print('| ' + i)
    return symbols


def add_to_default(symbols):
    print('Enter symbol to add: ')
    symbol = input().upper()
    while symbol != '':
        symbols.append(symbol)
        symbol = input('Enter symbol to add: Hit enter to quit')

def edit_default(symbols):
    print('Select symbol to delete: ')
    for i in range(1, len(symbols) + 1):
        print(f'{i} - {symbols[i-1]}')
    remove = symbols.pop(int(input())-1)
    print(f'{remove} removed')
    
def add_list():
    new_list = []
    print('Enter symbols to add: ')
    symbol = input().upper()
    while symbol != '':
        new_list.append(symbol)
        symbol = input('Enter symbol to add or enter to quit')
    while True:
        get_prices(new_list)
        print('CTRL + C to exit')

def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']


def main():
    run_program = True
    while run_program:
        print('Choose Options')
        for i in range(len(options)):
            print(f'{i+1} - {options[i]}')
        choice = int(input())
        if choice == 1:
            while True:
                print(get_prices(symbols))
                print('CTRL + C to quit')
                print()
                sleep(5)  # getting a new list of quotes every 5 seconds
        elif choice == 2:
            show_default(symbols)
        elif choice == 3:
            add_to_default(symbols)
        elif choice == 4:
            edit_default(symbols)
        elif choice == 5:
            add_list()
        elif choice == 6:
            run_program == False
        
if __name__ == "__main__":
    main()
        