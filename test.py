import random
couleur = ('pique', 'trefle', 'carreau', 'coeur')
valeur = ('as', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'valet', 'dame', 'roi')
cartes = []
for i in couleur:
            for n in valeur:
                cartes += [(n, i)]
                random.shuffle(cartes)
                

print(cartes)