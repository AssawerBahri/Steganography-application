from os import chdir,remove,getcwd   #Importation des procedures chdir,remove et getcwd du module os
from PIL import Image                #Importation de la bibliothéque PIL 


def enreg_img(mat,nom,fil):          #Définition de la fonction enreg_img
                                     #mat :une matrice de 3 dimensions contenant les pixels d'une image, nom :nom de l'image, fil :son repertoire
    rep_cour = getcwd()               
    liste=fil.split('/')             #Cette fonction permet d'enrigestrer l'image qui correspond à la matrice mat et l'enrigestrer ous le non nom dans le repertoire fil 
    chdir("/".join(liste))
    imgpil = Image.fromarray(mat)
    imgpil.save(nom+".bmp")
    

    chdir(rep_cour)

    
    
    
