from variables import cards, number_of_decks
from random import choice


def deck_config():
    '''
    Deck config: it will assign values for each card
    and include this one into deck.
    values:
    Face - > Card_face
    Value - > Card's value
    number_cards -> How many card's into deck
    '''
    deck = []
    card_values = {}
    for v in cards:
        card_values['face'] = v

        if v == 'A':
            card_values['value'] = [11, 1]
        elif isinstance(v, str):
            card_values['value'] = 10
        else:
            card_values['value'] = v

        card_values['number_cards'] = number_of_decks*4
        deck.append(card_values.copy())

    return deck


deck = deck_config()


def verifica_se_ainda_tem_carta():
    while True:
        new_card = choice(deck)
        if new_card['number_cards'] > 0:
            break
    return new_card


def subtrai_carta():
    # subtrai carta retirada
    # >>> essa funcao vai chamar a funcao verifica dentro dela
    card = verifica_se_ainda_tem_carta()
    for i, v in enumerate(deck):
        if card['face'] == v['face']:
            deck[i]['number_cards'] -= 1
    return card['face']


def name_validator(text):
    '''Verifiy if the name is valid'''
    while True:
        name = input(text).strip().capitalize()
        if name.isdigit() or name == '':
            print('❌ Please, enter a valid name.\n')
        else:
            break
    return name
