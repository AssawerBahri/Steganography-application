from scipy import misc                                                 #Importation de la bibliothéque scipy
import sys as sys                                                      #Importation du module sys
from os import chdir,getcwd



def lecture_img(filI):                                                 #Définition de la fonction
                                                                       #filI: le chemin de l'image 
    try:
        
        liste1=filI.split('/')                                         #Cette fonction permet de ouvrir l'image dont le chemin est filI                                          
        rep_cour = getcwd()                                            #et de retourner la matrice de pixels qui lui correspond 
        liste2=rep_cour.split('\\')
        
        if '/'.join(liste2)!='/'.join(liste1[0:len(liste1)-1]):
            chdir('/'.join(liste1[0:len(liste1)-1]))
        mat = misc.imread(liste1[len(liste1)-1])

        chdir( '/'.join(liste2))
        
        return mat

    except IOError:
    

        sys.exit(1)





