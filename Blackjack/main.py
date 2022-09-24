'''This is a game of Blackjack'''

import os
from random import choice, choices
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def total(cards):
    '''Calulate the total of hand'''
    total = 0
    for i in cards:
        total += i
    return total

def cards_on_table():
    '''Print the dealer and player hand, and hand value at end of game'''
    print('Dealer hand',dealer,'Total', total(dealer))
    print('Player hand',player,'Total', total(player))
    print()


player_total = 0
dealer_total = 0

# print (logo)
# print('Welcome')

game_on = True
while True:

    print (logo)
    print('Welcome')

    player = []
    dealer = []

    player += choices(cards, k=2)
    dealer += choices(cards, k=2)


    while game_on:
        print ('Dealer hand', dealer[0])
        print ('Player hand', player)

        if total(player) == 21 and len(player) == 2:
            print('Player get a blackjack.\nPlayer Win.\n')
            cards_on_table()
            break

        hit_or_stand = input('Do you want to hit or stand\n').lower().strip()
        if hit_or_stand not in ['hit','stand']:
            print('Plese pick a choice')

        elif hit_or_stand == 'hit':
            card = choice(cards)
            player.append(card)

            if 11 in player and total(player)> 21:
                player.remove(11)
                player.append(1)

            if total(player) > 21:
                print('Player goes over 21.\nPlayer Lose.')
                cards_on_table()
                break

            if total(player) == 21 and len(player) == 2:
                print('Player get a blackjack.\nPlayer Win.')
                cards_on_table()
                break

        elif hit_or_stand == 'stand':
            while True:
                if total(dealer) < 17:
                    card = choice(cards)
                    dealer.append(card)
                    if 11 in dealer and total(dealer) > 21:
                        dealer.remove(11)
                        dealer.append(1)

                    if total(dealer) > 21 :
                        print('Dealer Bust.\nDealer Lose.')
                        cards_on_table()
                        game_on = False
                        break

                    if total(dealer) > total(player) and total(dealer) < 21:
                        print('Dealer Win.')
                        cards_on_table()
                        game_on = False
                        break
                else:
                    if total(dealer)> total(player):
                        print('Dealer Win.')
                        cards_on_table()
                        game_on = False
                        break

                    print('Dealer Bust.\nDealer Lose.')
                    cards_on_table()
                    game_on = False
                    break

    new_game = input('Do you want to start a new game? y or n\n').lower()
    while new_game not in ['y','n']:
        print('Plese make a choice.')
    if new_game == 'y':
        os.system('cls')
        game_on = True
    elif new_game == 'n':
        break
