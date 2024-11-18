def english_learn(n: int, fri: list[str], eni: list[str]):
    fr=["manger", "dormir"]
    en=["eat", "sleep"]
    if (fri!=None) and (eni!=None):
        fr=["manger", "dormir"]
        fr.extend(fri)
        en=["eat", "sleep"]
        en.extend(eni)
    if (len(fr)!=len(en)):
        print("Erreur 404")
        return False
    x = len(fr)
    z = 0
    cho=0
    nul=0
    for i in range(n):
        z += 1
        x = len(fr) - z
        print(str(fr[x]))
        if (input()!=str(en[x])):
            print( "Faux c'est \""+ str(en[x]) +"\" avec \""+ str(fr[x]) + "\"!")
            nul+=1
        else:
            print("Bonne reponse!")
            cho+=1
    moy=cho/n*100
    print(f"Vous avez fait {cho} bonne reponse et {nul} mauvaise reponse!!" )
    print(f"Ce qui te fais un taux de reussite de {moy}%" )
    if(moy==100):
        print("Tu es le GOAT que tu pense etre!!")
    elif (moy>=75):
        print("Tu obtiens un A+")
    elif(moy>=50):
        print("Tu obtiens un A")
    elif(moy>=25):
        print("Tu obtiens un A-")
    elif(moy>=0):
        print("Tu obtiens un A--")
    elif(moy==0):
        print("Tu es vraiment GUEZ")
    return None

def update_learn(fri: list[str], eni: list[str]):
    fr=["manger", "dormir"]
    fr.extend(fri)
    en=["eat", "sleep"]
    en.extend(eni)
    print(str(fr))
    print(str(en))

def english_learn1(n: int, fri: list[str], eni: list[str]):
    fr=["manger", "dormir"]
    en=["eat", "sleep"]
    if (fri!="0" ) and (eni!="0"):
        fr=["manger", "dormir"]
        fr.extend(fri)
        en=["eat", "sleep"]
        en.extend(eni)
    if (len(fr)!=len(en)):
        print("Erreur 404")
        return False
    x = len(fr)
    z = 0
    cho=0
    nul=0
    for i in range(n):
        z += 1
        x = len(fr) - z
        print(str(en[x]))
        if (input()!=str(fr[x])):
            print( "Faux c'est \""+ str(fr[x]) +"\" avec \""+ str(en[x]) + "\"!")
            nul+=1
        else:
            print("Bonne reponse!")
            cho+=1
    moy=cho/n*100
    print(f"Vous avez fait {cho} bonne reponse et {nul} mauvaise reponse!!" )
    print(f"Ce qui te fais un taux de reussite de {moy}%" )
    if(moy==100):
        print("Tu es le GOAT que tu pense etre!!")
    elif (moy>=75):
        print("Tu obtiens un A+")
    elif(moy>=50):
        print("Tu obtiens un A")
    elif(moy>=25):
        print("Tu obtiens un A-")
    elif(moy>0):
        print("Tu obtiens un A--")
    elif(moy==0):
        print("Tu es vraiment GUEZ")

    return None

