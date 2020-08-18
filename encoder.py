from tkinter import *                        #Importation de la bibliothéque tkinter (Tool kit interface)
from tkinter import filedialog,messagebox    #Importation des procedures filedialog et massagebox de la bibliothéque tkinter
from principal import *                      #Importation des fonctions écrites dans le fichier 'principal' 
from lecture_image import lecture_img        #Importation de la fonction lecture_img du fichier lecture_image
import sys as sys                            #Importation du modume sys
import matplotlib.pyplot as plt              #Importation de la bibliothéque matplotlib



def filef():                                                                  #Définition de la fonction filef
    global filf               
                                                                              #Cette fonction permet de recupérer l'emplacement d'un fichier texte    
                                                                              #ouvert à l'aide de l'interface graphique
    filf=filedialog.askopenfilename(filetypes = [("Fichiers TXT","*.txt")])

    wid = Label(encoder, text=filf)
    wid.config(bg='RosyBrown2', fg='red')
    wid.place(x='170',y='150')
    


def fileI():                                                                  #Définition de la fonction fileI              
    global filI
    filI=filedialog.askopenfilename(filetypes = [("Fichiers BMP","*.bmp")])   #Cette fonction permet de recupérer l'emplacement d'une image bmp
    wid = Label(encoder, text=filI)                                           #ouverte à l'aide de l'interface graphique
    wid.config(bg='RosyBrown2', fg='red')
    wid.place(x='170',y='290')

           
    
def file():                                                                   #Définition de la fonction file                                            
    global fil
                                                                              #Cette fonction permet de recupérer l'emplacement d'un dossier 
    fil=filedialog.askdirectory()
    wid = Label(encoder, text=fil)
    wid.config(bg='RosyBrown2', fg='red')
    wid.pack()

def saisie():                                                                 #Définition de la fonction saisie        
    global nom
    nom=entree.get()                                                          #Cette fonction permet de recupérer une entrée texte
    


def visimage():                                                               #Définition de la fonction visimage (visualiser image)

    try:                                                                      #Cette fonction permet de visualiser l'image après encodage 
                                                                              #Elle retourne un message d'erreur si aucune image n'est encore encodée
        mat=lecture_img(filI)                                                 
        plt.imshow(mat)
        plt.axis('off')
        plt.show()
    except:
        encod=Tk()
        encod.geometry("0x0+560+430")
        messagebox.showwarning("Warning","Aucune image n'est encore codée \nVeuillez remplir tous les champs!")
        encod.destroy()
        encod.mainloop()
    
        
        
       
        


nom=str()
filf=str() #des variables globales pour la recupération des données saisies par l'utilisateur
filI=str()
fil=str()

        
encoder=Tk()                                                            #ligne 72 ------>>ligne 160 la réalisation de l'interface graphique 
encoder.geometry("550x550+300+100")
encoder.title("Encoder")
encoder['bg']='RosyBrown2'


labelfont = ('times', 20,'bold')

#fichier

widget = Label(encoder, text='Ouvrir le fichier texte:')    
widget.config(bg='RosyBrown2', fg='black')  
widget.config(font=labelfont)
widget.pack(pady =20)                                                    #Bouton pour exécuter la fonction filef() 


photo1 = PhotoImage(file='ouvrir.png')

boutouv = Button(encoder, image=photo1,command=filef)
boutouv.config(width=90,height=60)
boutouv.pack()



#image

widget = Label(encoder, text="Ouvrir l'image Bitmap:")
widget.config(bg='RosyBrown2', fg='black')                               #Bouton pour exécuter la fonction fileI()
widget.config(font=labelfont)
widget.pack(pady =20)


boutouv = Button(encoder, image=photo1,command=fileI)
boutouv.config(width=90,height=60)
boutouv.pack()

#enregistrer

photo2 = PhotoImage(file='enreg.png')

                                                                       
widget = Label(encoder, text="Enregistrer l'image codée :")
widget.config(bg='RosyBrown2', fg='black')               
widget.config(font=labelfont)
widget.pack(pady =20)

labfont = ('times', 12,'bold')
wid = Label(encoder, text="Entrer le nom de la nouvelle image :")
wid.config(bg='RosyBrown2', fg='black')
wid.config(font=labfont)
wid.pack(side=TOP)




entree = Entry(encoder)                                                  #Une zone pour écrire un texte
entree.pack()

 
bout = Button(encoder, text = 'valider', command = saisie,width=5)       #Bouton pour exécuter la fonction saisie()
bout.config(fg='blue',bg='VioletRed2')
bout.config(font=('verdana',10))
bout.pack()




boutouv = Button(encoder, image=photo2,command=file)                     #Bouton pour exécuter la fonction file()
boutouv.config(width=90,height=60)
boutouv.pack(pady=10)

#quitter

bouton3=Button(encoder, text='Quitter', command = encoder.destroy,width=5,height=1)
bouton3.config(fg='blue',bg='VioletRed2')                                #Bouton pour quitter l'interface
bouton3.config(font=('verdana',12))
bouton3.place(x='450',y='500')

#visulisation de l'image

photo3 = PhotoImage(file='voir.png')

bouton3=Button(encoder, image=photo3,command = visimage,width=54,height=30)
bouton3.config(fg='blue',bg='VioletRed2')
bouton3.config(font=('verdana',12))                                      #Bouton pour exécuter la fonction visimage()
bouton3.place(x='450',y='460')


encoder.mainloop()


i=1

try:                                                                     #L'essai de l'exécution de la fonction principal() avec affichage des messages 
                                                                         #selon l'entier retourné par cette fonction (opération réussie,erreur ou attention)  
    i=principal(nom,filf,filI,fil)
    if i==0:
        print(0/0)
        
    encoder=Tk()
    encoder.geometry("0x0+560+430")
    messagebox.showinfo('Encodage réussi',"Le fichier est encodé avec succès" )
    encoder.destroy()
    encoder.mainloop()
    
except :
    
    encoder=Tk()
    encoder.geometry("0x0+560+430")
    if i==0:
        messagebox.showerror("Error", "L'image ne peut pas supporter le fichier texte!")
    else:
        messagebox.showwarning("Warning","Aucun fichier n'est codée \nVeuillez remplir tous les champs!")
  
    
    encoder.destroy()
    encoder.mainloop()
    
    sys.exit(1)


