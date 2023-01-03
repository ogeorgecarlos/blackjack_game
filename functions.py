import random
from variables import number_of_decks


def header(text):
    '''Create a pattern headers for the system'''
    print()
    print(60*'-')
    print(f'{text:^60}')
    print(60*'-')
    print()


def name_validator(text):
    '''Verifiy if the name is valid'''
    while True:
        name = input(text).strip().capitalize()
        if name.isdigit() or name == '':
            print('❌ Please, enter a valid name.\n')
        else:
            break
    return name


def deck_config():
    '''
    Deck config: it will assign values for each card
    and include this one into deck.
    ...
    "value" -> Card's value
    "number_cards" -> How many card's into the deck
    '''
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'J', 'Q']
    deck = {}
    card_values = {}
    for i in cards:
        deck[i] = card_values

        if i == 'A':
            card_values['value'] = [11, 1]
        elif isinstance(i, str):
            card_values['value'] = 10
        else:
            card_values['value'] = i

        card_values['number_cards'] = number_of_decks*4
        deck[i] = card_values.copy()
    return deck


deck = deck_config()


def subtrai_carta():
    # verifica se a carta escolhida ainda tem dispon no deck
    while True:
        new_card = random.choice(list(deck))
        if deck[new_card]['number_cards'] > 0:
            break
    # subtrai do deck a nova carta
    for i in list(deck):
        if i == new_card:
            deck[i]['number_cards'] -= 1
    return new_card
