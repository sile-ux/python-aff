import datetime

date=int(input("entrer votre anne de naissance:"))
nom=input("entez votre nom:")
ville=input("dans quel ville vivez vous:")
date_act=datetime.date.today().year
age=(date_act-date)
print("bonjour",nom,"\nvous avez",age,"ans","\nvous habitez a :",ville)