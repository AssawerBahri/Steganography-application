def decimalbinaire(des,cond=0):                     #Définition de la fonction decimalbinaire 
                                                    #des: un entier présentant un nombre en decimal,
    if des==0:                                      #cond: un entier par défaut 0 présentant une condition sur le retour de la fonction
        res='0'
    else:                                           #Cette fonction permet de convertir un nombre decimal en binaire 
        quotient=des                                #Elle retourne le nombre binaire sur 8 bits si cond=0 et sur 2 bits si cond=1
        liste=[]
        res=""
    
        while quotient!=1:
            liste=liste+[quotient%2]
            quotient=quotient//2
        liste=liste+[1]
    
        while liste!=[]:
            res=res+str(liste[-1])
            liste=liste[:-1]
    if cond==0:
        while len(res)<8:
            res='0'+res
    else:
        while len(res)<2:
            res='0'+res
    
    return res




def binairedecimal(bin):                           #Définition de la fonction binairedecimal 
                                                   #bin: chaine de caractère présentant un nombre decimal
    des=0;
    for i in range(len(bin)-1,-1,-1):
        if (bin[i]=='1'):                          #Cette fonction permet de convertir un nombre binaire en decimal 
            des+=2**(len(bin)-i-1)

    return(des)
        



class CracC:                                                                    #Définition de la classe CracC(caractére codé)
    def __init__(self,l):                                                       #Un objet de cette classe présente un caractère en train d'être coder 
        self.orig=l                                                             #Ses attributs sont orig: le cractére lui même  
        self.asci=ord(l)                                                        #                   asci: son code asci
        self.bin=decimalbinaire(self.asci)                                      #                   bin : le code asci en binaire
        self.noncode=self.bin                                                   #                   noncode: les bits de bin qui ne sont pas encore cachés dans l'image
        self.code=self.noncode[len(self.noncode)-2:len(self.noncode)]           #                   code   : les deux bits qui vont être chachés


    def codage(self):                                                           #Définition de la méthode codage du classe CracC
        self.noncode=self.noncode[0:len(self.noncode)-2]                        #Cette méthode permet d'actualiser les attributs noncode et code   
        self.code=self.noncode[len(self.noncode)-2:len(self.noncode)]           #à chaque fois deux bits de bin sont déja codés          
        



class CracD:                                                                    #Définition de la classe CracD(caractére decodé)
    def __init__(self):                                                         #Un objet de cette classe présente un caractère en train d'être decoder 
        self.orig=''                                                            #Ses attributs sont orig: le cractére lui même
        self.asci=0                                                             #                   asci: son code asci 
        self.bin=str()                                                          #                   bin : le code asci en binaire


    def codage(self,m):                                                         #Définition de la méthode codage du classe CracD
        self.bin=decimalbinaire(int(m)%4,1)+self.bin                            #Cette méthode permet d'actualiser l'attribut bin
                                                                                #à chaque fois les deux bits cachés dans une cellule m de la matrice image sont décodés 


    def caractere(self):                                                        #Définition de la méthode caractere du classe CracD
        self.asci=binairedecimal(self.bin)                                      #Cette méthode permet de trouver le code asci du caractère décodé et son caractère   
        self.orig=chr(self.asci)                                                #à-partir du nombre binaire trouver



    def reset(self):                                                           #Définition de la méthode reset du classe CracD 
        self.bin=str()                                                         #Cette  méthode affecte à bin une chaine vide pour réutiliser l'objet





