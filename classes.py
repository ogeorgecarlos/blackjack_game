from functions import name_validator, subtrai_carta


class User:
    # faz a classe
    def __init__(self):
        self.name = name_validator('exemplo')
        self.cards = [subtrai_carta(), subtrai_carta()]
        self.hand = 0
