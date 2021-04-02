
import random
class Pokemon():
    def __init__(self, nom,  nature, nom_attaque,Degat_attaque, pv):
        self.nom = nom
        self.nature  = nature
        self.nom_attaque = nom_attaque
        self.Degat_attaque = Degat_attaque
        self.pv  = pv

    def combat(self):
        p2.pv -= p1.Degat_attaque

        print(p1.nom,p1.pv,"attaque",p1.nom_attaque)
        p2.pv -= p1.Degat_attaque
        print(p2.nom,p2.pv,"attaque",p2.nom_attaque)
        p1.pv -= p2.Degat_attaque        
        if (p1.pv > 0) and (p2.pv > 0):
            p1.combat()
        else:
            if(p1.pv > p2.pv):
                print(p1.nom, "gagne")
            else:
                print(p2.nom, "gagne")





p1 = Pokemon("salameche", "feu", "flammeche",2, 20)
p2 = Pokemon("carapute", "eau", "eclaboussure",2, 20)

p1.combat()