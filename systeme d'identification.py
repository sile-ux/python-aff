user={}
def regis():
    mcl= input("entrez votre nom:")
    pswr=int(input("entrer votre numero:"))
    if mcl and pswr in user:
        print("cet utilisateur est deja enregister!")
    else:
        user[mcl]=pswr
        print("utilisateur enregistrer!")
def rechercher():

    nom=input("entrez le nom")
    if nom == mcl :
        print(pswr)
    elif num==pswr:
        print(mcl)
    else:
        print("mots cle ou mots de passe incorect ressayer")

def menu():
    while True:
        print("MENU:")
        print("1:s'enregistrer")
        print("2:rechercher")
        print("3:quitter")
        choix=input("entez votre choix:")

        if choix=="1":
            regis()
        elif choix=="2":
            rechercher()

        elif choix=="3":
            break
        else:
         print("entrez la bonne touche:")
        
menu()









