X = 0
Y = 10
finish = False
while (finish == False):
    saisie = input('saisissez votre chiffre')
    if((int(saisie) >= X) and (int(saisie) <= Y)):
        finish = True
        print("merci")
    else:
        print("mauvais choix veuillez rentrer un entier entre 1 et 10")
