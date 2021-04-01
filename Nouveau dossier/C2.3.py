import math
p1 = input('saisissez p')
p2 = input('saisissez v')
pSeuil =  2.3
vSeuil = 7.41
if(int(p1) > pSeuil) and (int(p2) > vSeuil):
    print("arret immediat")
elif(int(p2) > vSeuil):
    print("augmenter le volume ed l'enceinte")
elif(int(p1) > pSeuil):
    print("diminuer le volume ed l'enceinte")
else:
    print("tout va bien")