from functions import deck, subtrai_carta
from classes import User

# config player
user = User()
print(user.cards)

# config user.hand (issovai ficar def da class)
for i in user.cards:
    for j in deck:
        if i == j['face'] and i != 'A':
            user.hand += j['value']
        elif i == j['face'] and i == 'A':
            if user.hand + j['value'][0] > 21:
                user.hand += j['value'][1]
            else:
                user.hand += j['value'][0]


# exibir cartas dos jogadores
print(f'{user.name}, suas cartas são {user.cards} com o total de {user.hand}')

# perguntar se quer jogar novamente
while True:
    decision = input('y or n: ').strip()
    if decision in "Yy":
        user.cards.append(subtrai_carta())
        print(f'{user.name}, suas cartas são {user.cards} com o total de {user.hand}')
        print(deck)
    else:
        break
