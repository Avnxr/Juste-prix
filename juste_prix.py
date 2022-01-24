from random import randint

def main():

    # Statut de jeu
    running = True

    # Choisir un nombre entre 1 et 1000
    just_price = randint(1, 100)

    # Tant que le jeu n'est pas fini

    while running:

        # Demander à l'utilisateur de trouver un prix
        user_price = int(input("Entrez un prix : "))

        # Si le prix est le meme que le juste prix
        if user_price == just_price:
            print("Trouvé ! Le juste prix était bien ", just_price)
            # fin du jeu
            running = False

        # Si le prix de l'utilisateur est supérieur au prix à trouver
        elif user_price > just_price:
            print("C'est moins !")

        # Si le prix de l'utilisateur est inférieur au prix à trouver
        elif user_price < just_price:
            print("C'est plus !")

    # Fin du jeu après la boucle
    print("Fin du jeu !")


if __name__ == '__main__':
    main()
