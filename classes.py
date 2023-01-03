from functions import name_validator, subtrai_carta, deck


class User:
    # faz a classe
    def __init__(self):
        self.name = name_validator('✅ Enter your name: ')
        self.cards = []
        self.score = 0

    def first_cards(self):
        '''Choice a couple of cards to player'''
        for _ in range(2):
            self.cards.append(subtrai_carta())
        self.update_score()

    def get_card(self):
        '''Get one more card to player'''
        new_card = subtrai_carta()
        self.cards.append(new_card)
        self.update_score()

    def update_score(self):
        '''Up todate the player's total score'''
        self.score = 0
        for i in self.cards:
            if i == 'A':
                if self.score + deck[i]['value'][0] > 21:
                    self.score += deck[i]['value'][1]
                else:
                    self.score += deck[i]['value'][0]
            else:
                self.score += deck[i]['value']


class Dealer:
    # faz o dealer
    def __init__(self):
        self.name = 'Dealer'
        self.initial_cards = []
        self.cards = []
        self.score = 0

    def first_cards(self):
        '''Choice a couple of cards to Dealer'''
        card1 = subtrai_carta()
        card2 = subtrai_carta()
        self.cards.append(card1)
        self.cards.append(card2)
        self.initial_cards.append(card1)
        self.initial_cards.append('🔗')
        self.update_score()

    def get_card(self):
        '''Get one more card to Dealer'''
        new_card = subtrai_carta()
        self.cards.append(new_card)
        self.update_score()

    def update_score(self):
        '''Up todate the player's total score'''
        self.score = 0
        for i in self.cards:
            if i == 'A':
                if self.score + deck[i]['value'][0] > 21:
                    self.score += deck[i]['value'][1]
                else:
                    self.score += deck[i]['value'][0]
            else:
                self.score += deck[i]['value']
