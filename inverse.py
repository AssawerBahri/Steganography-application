from lecture_image import lecture_img                   #Importation de la fonction lecture_img du fuchier lecture_image

from fichier import ecriture_fich                       #Importation de la fonction ecriture_fich du fichier fichier

from classCaractere import *                            #Importation de la classe CracD

from os import chdir,getcwd                             #Importation de chdir et getcwd du module os


def inverse(nom,filI,fil):                              #Définition de la fonction inverse
                                                        #nom: le nom du nouveau fichier texte, filI: le chemin de l'image codée, fil: le repertoire de fichier 'nom'
    rep_cour = getcwd()                        
                                                        #Cette fonction permet d'analyser une image qui cache un texte 
    mat=lecture_img(filI)                               #Decode le texte caché et l'enregistrer d'un fichier sous le nom 'nom' dans le repertoire 'fil'

    fich=ecriture_fich(nom,fil)

    dim=mat.shape


    marq_fin='§'
    cont=0
    tompon=CracD()

    for i in range(dim[0]):
        for j in range(dim[1]):
            for k in range(dim[2]):
            
                tompon.codage(mat[i,j,k])
                cont+=1
        
                if cont==4:
                    tompon.caractere()

                    if tompon.orig==marq_fin:
                        break
                    else:
                        
                        fich.write(tompon.orig)
                        cont=0
                        tompon.reset()
                if tompon.orig==marq_fin:
                        break
                
            if tompon.orig==marq_fin:
                break
        
        if tompon.orig==marq_fin:
            break
    
    fich.close()
    

    chdir(rep_cour)
    
        
            
        
        
