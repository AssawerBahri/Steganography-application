from lecture_image import lecture_img                   #Importation de la fonction lecture_img du fichier lecture_image

from fichier import lecture_fich                        #Importation de la fonction lecture_fich du fichier fichier

from enreg_img import enreg_img                         #Importation de la fonction enreg_img du fichier enreg_img

from classCaractere import *                            #Importation de la classe CracC et ses méthodes du fichier classCaractere                           





def dissimuler(f,m):                                    #Définition de la fonction dissimuler 
    
  aux=int(f[1])+int(f[0])*2                             # f: un chaine de deux cractères prensentant un nombre binaire de deux bits, m:un nombre en decimal 

  return m//2*2+aux                                     #La fonction permet de changer les deux derniers bits de m en binaire par f et retourne son entier

  




def principal(nom,filf,filI,fil):                      #Définition de la fonction principal
                                                       # nom: Le nom de la nouvelle image, filf: Le chemin du fichier texte, filI: Le chemin de l'image Bitmap,  
                                                       # fil: Le chemin d'enregistrement de la nouvelle image

  mat=lecture_img(filI)                                #Cette fonction permet de cacher le texte dont le chemin est filf dans l'image dont le chemin est filI 
                                                       #et enregistrer l'image modifier dans fil sous le nom nom
  fich=lecture_fich(filf)                              #Elle retourne un enier: 0 si l'image choisie ne peut pas supporter le fichier texte, 1 si l'encodage est fait avec succès  

  dim=mat.shape

  if dim[0]*dim[1]*dim[2]<(len(fich)+1)*4:
    return 0
   

  cont=0
  controle=0
  test=0
  let=CracC(fich[cont])
  marq_fin='§'

  for i in range(dim[0]):
    for j in range(dim[1]):
      for k in range(dim[2]):
    
        mat[i,j,k]=dissimuler(let.code,mat[i,j,k])
      
        let.codage()
        controle+=1
        if  controle==4:
          controle=0
          cont+=1
          if cont==len(fich):
            let=CracC(marq_fin)
          elif cont<len(fich):
            let=CracC(fich[cont])
      
          
        if cont==len(fich)+1:
          break
      if cont==len(fich)+1:
        break
  
    if cont==len(fich)+1:
      break

  enreg_img(mat,nom,fil)
  return 1
  
        

       
  





