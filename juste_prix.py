from random import randint


def price():

    just_price = randint(1, 100)

    running = True

    while running:

        user_price = int(input("Choississez un prix"))
        
        if(user_price == just_price):
            print("Bravo ! Vous avez bien trouvé", just_price)
            running = False

        elif user_price > just_price:
            print("C'est moins !")

        elif user_price < just_price:
            print("C'est plus !")

    print("Fin du jeu")


if __name__ == '__main__':
    price()
