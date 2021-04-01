import math
mot1 = input('saisissez un mot \n')
mot2 = input('saisissez un autre mot \n')
MAJ1 = 0
MAJ2 = 0
if(ord(mot1[0]) < 97):
    MAJ1 = 20
else:
    MAJ1 = 0
if(ord(mot2[0]) < 97):
    MAJ2 = 20
else:
    MAJ2 = 0

if(ord(mot1[0])+ MAJ1 > ord(mot2[0])+MAJ2):
    res = "the second word comes before the first one" 
else:
    res = "the first word comes before the second one"
print(res)