# -*- coding: utf-8 -*-
"""Formule

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KO_m0ckSwVikopImlZPnTTSkkrNhUzDu
"""


TK:float;
TH:float;
TJ:float;
credit:bool;
total:float;
s:float;
s=0;
Nbre_Klm:float;
Nbre_Klm=0;
credit='';
a:str;
b:str;
c:str;
d:str;
a='';
b='';
c='';
d='';

Nbre_Klm = float(input("Quel est le nombre de klm parcouru ? "));
temps_trajet = float(input("Quel est le temps en service ? "));
temps_attente = float(input("Quel est le temps d'attente ? "));

Temps_service = temps_trajet + temps_attente;
print( Temps_service );

print(" a: partner \n b: fourgon ou bien camionnette \n c: camionnette2 \n d: poids lourds\n")
vihecule = str(input("Quel est le type de votre vehicule ? "))
if vihecule == "a":
  print("votre vehicule est une partner")
elif vihecule == "b":
  print("votre vehicule est un fourgon ou bien camionnette")
elif vihecule == "c":
  print("votre vehicule est une camionnette2")
elif vihecule == "d":
  print("votre vehicule est de type poids lourds")
else:
  print("Reponse invalide")

credit_vihecule = str(input("Tapez OUI si votre vehicule est en credit si non tapez NON \n "))
if credit_vihecule == "non":
  credit = False
  print("vihecule en comptant : ", credit)
elif credit_vihecule == "oui":
  credit = True
  print("vihecule en credit :", credit)
else:
  print("réponse incorrecte")

if ((credit  == True) and (vihecule == "a" )):
  TK = 0.14435 * Nbre_Klm
  print(TK)
  TH = (temps_trajet + temps_attente) * 3.7
  print(TH)
  TJ = (Temps_service * 119.3) / 8.43
  print(TJ)
  total = TK+TH+TJ
  print("Total = ", total);
elif ((credit  == False) and (vihecule == "a" )):
  TK = 0.14435 * Nbre_Klm
  print(TK)
  TH = (temps_trajet + temps_attente) * 3.7
  print(TH)
  TJ = (Temps_service * 87.96) / 8.43
  print(TJ)
  total = TK+TH+TJ
  print("Total = ", total)
elif ((credit  == True) and (vihecule == "b" )):
  TH = (temps_trajet + temps_attente) * 3.7;
  TJ = (Temps_service * 201.03 ) / 8.43;
  TK = 0.23005 * Nbre_Klm
  print(TK)
  print(TH)
  print(TJ)
  total = TK+TH+TJ
  print("Total = ", total);
elif ((credit  == False) and (vihecule == "b" )):
  TK = 0.23005  * Nbre_Klm;
  TH = (temps_trajet + temps_attente) * 3.7;
  TJ = (Temps_service * 138.35) / 8.43;
  print(TK)
  print(TH)
  print(TJ)
  total = TK+TH+TJ
  print("Total = ", total)
elif ((credit  == True) and (vihecule == "c" )):
  TK = 0.28505  * Nbre_Klm;
  TH = (temps_trajet + temps_attente) * 3.7;
  TJ = (Temps_service * 214.16 ) / 8.43;
  print(TK)
  print(TH)
  print(TJ)
  total = TK+TH+TJ
  print("Total = ", total);
elif ((credit  == False) and (vihecule == "c" )):
  TK = 0.23005  * Nbre_Klm;
  TH = (temps_trajet + temps_attente) * 3.7;
  TJ = (Temps_service * 182.72) / 8.43;
  print(TK)
  print(TH)
  print(TJ)
  total = TK+TH+TJ
  print("Total = ", total)
elif ((credit  == True) and (vihecule == "d" )):
  TK = 0.7106  * Nbre_Klm;
  TH = (temps_trajet + temps_attente) * 3.7;
  TJ = (Temps_service * 320.52 ) / 8.43;
  print(TK)
  print(TH)
  print(TJ)
  total = TK+TH+TJ
  print("Total = ", total);
elif ((credit  == False) and (vihecule == "d" )):
  TK = 0.7106  * Nbre_Klm;
  TH = (temps_trajet + temps_attente) * 3.7;
  TJ = (Temps_service * 226.5) / 8.43;
  print(TK)
  print(TH)
  print(TJ)
  total = TK+TH+TJ
  print("Total = ", total)
else: print("vérifiez les champs")

print("prix conseilé est :", total*1.2)

