import sys as sys                                                         #Importation du module sys
from os import chdir,getcwd                                               #Imprtation des procedure chdir et getcwd du module os



def lecture_fich(filf):                                                   #Définition de la fonction lecture_fich     
                                                                          #filf: chemin du fichier texte
    try:
                                                                          #Cette fonction permet d'ouvrir le fichier et retourner son contenu
        liste1=filf.split('/')
        rep_cour = getcwd()
        liste2=rep_cour.split('\\')
        
        if '/'.join(liste2)!='/'.join(liste1[0:len(liste1)-1]):
            chdir('/'.join(liste1[0:len(liste1)-1]))

        fichier=open(liste1[len(liste1)-1],'r')
                  
        f=fichier.read()
        fichier.close()
        chdir('/'.join(liste2))
        return f
 
    except IOError:

      print( 'Erreur sur ouverture du fichier texte ') 

      sys.exit(1)



def ecriture_fich(nom,fil):                                               #Définition de la fonction ecriture_fich
                                                                          #nom: nom de fichier ,fil: son repertoire    
        
    try:                                                                  #Cette fonction permet de créer un fichier sous le nom nom et retourner son identifiant 
    
        
        liste=fil.split('/')
        chdir("/".join(liste))

        fichier=open(nom+".txt",'a','UTF-8')
        return fichier
 
    except IOError:

        sys.exit(1)
        

