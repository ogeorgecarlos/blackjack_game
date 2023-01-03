from sys import exit
from time import sleep
from classes import Dealer, User
from functions import header

# >Main program<

header("♠ Let's start!")

user = User()
user.first_cards()
dealer = Dealer()
dealer.first_cards()

header("♠ The beginning.... ")

print(f'✅ {user.name}, your cards is {user.cards} and total score is {user.score}')
print(f"\n✅ The {dealer.name}'s cards is {dealer.initial_cards}.")


header("♠ Let's continue?")
while True:
    choice = input('✅ Do you want get one more card ,Y or N?\n').strip()
    if choice in "yY":
        user.get_card()
        if user.score > 21:
            header('😢You loose...')
            print(
                f'❌ You current cards is {user.cards}, {user.score} total scores')
            print(
                f"❌ The Dealer's card was {dealer.cards}, {dealer.score} total scores")
            print()
            exit()
        else:
            header('♠ Updating...')
            print(
                f'\n✅ You current cards is {user.cards}, {user.score} total scores\n')
            print(f"\n✅ The {dealer.name}'s cards is {dealer.initial_cards}.")
    elif choice in "nN":
        while True:
            if dealer.score < 16:
                dealer.get_card()
                header('⏳ The Dealer is geting a new card...')
                sleep(1)
            elif dealer.score > 21:
                header("🤣 You Win...")
                print(
                    f'✅ You current cards is {user.cards}, {user.score} total scores\n')
                print(
                    f"❌ The Dealer's card was {dealer.cards}, {dealer.score} total scores\n")
                print()
                exit()
            elif dealer.score >= 16 and user.score > dealer.score:
                header("🤣 You Win...")
                print(f'✅ You current cards is {user.cards}, {user.score} total scores\n')
                print(f"❌ The Dealer's card was {dealer.cards}, {dealer.score} total scores\n")
                print()
                exit()
            else:
                header('😢You loose...')
                print(f'❌ You current cards is {user.cards}, {user.score} total scores')
                print(f"✅ The Dealer's card was {dealer.cards}, {dealer.score} total scores")
                print()
                exit()
