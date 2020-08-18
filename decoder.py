from tkinter import *                                           #Importation de la bibliothéque tkinter (Tool kit interface)
from tkinter import filedialog,messagebox                       #Importation des procedures filedialog et massagebox de la bibliothéque tkinter
from inverse import inverse                                     #Importation de la fonction inverse() du fichier 'inverse'



def file():                                                     #Définition de la fonction file
    global fil                                                  
                                                                #Cette fonction permet de recupérer l'emplacement d'un dossier
    fil=filedialog.askdirectory()

    wid = Label(decoder, text=fil)
    wid.config(bg='RosyBrown2', fg='red')
    wid.pack()



def fileI():                                                    #Définition de la fonction fileI                                                  
    global filI
                                                                #Cette fonction permet de recupérer l'emplacement d'une image bmp
                                                                #ouverte à l'aide de l'interface graphique
    filI=filedialog.askopenfilename(filetypes = [("Fichiers BMP","*.bmp")])
    
    wid = Label(decoder, text=filI)
    wid.config(bg='RosyBrown2', fg='red')
    wid.place(x='180',y='150')


def saisie():                                                    #Définition de la fonction saisie
                                                                 
    global nom                                                   #Cette fonction permet de recupérer une entrée texte
    nom=entree.get()


    




nom=str()
          #des variables globales pour la recupération des données saisies par l'utilisateur
fil=str()





decoder=Tk()                                                     #ligne 48 ------>>ligne 115 la réalisation de l'interface graphique
decoder.geometry("550x550+300+100")
decoder.title("Decoder")
decoder['bg']='RosyBrown2'



labelfont = ('times', 20,'bold')


photo1 = PhotoImage(file='ouvrir.png')

widget = Label(decoder, text="Ouvrir l'image Bitmap:")
widget.config(bg='RosyBrown2', fg='black')  
widget.config(font=labelfont)
widget.pack(pady =20)


boutouv = Button(decoder, image=photo1,command=fileI)            #Bouton pour exécuter la fonction fileI()
boutouv.config(width=90,height=60)
boutouv.pack()

photo2 = PhotoImage(file='enreg.png')


widget = Label(decoder, text="Enregistrer le fichier decodé :")
widget.config(bg='RosyBrown2', fg='black')  
widget.config(font=labelfont)
widget.pack(pady =40)

labfont = ('times', 12,'bold')
wid = Label(decoder, text="Entrer le nom du nouveau fichier :")
wid.config(bg='RosyBrown2', fg='black')
wid.config(font=labfont)
wid.pack(side=TOP)




entree = Entry(decoder)                                           #Une zone pour écrire un texte
entree.pack()

 
bout = Button(decoder, text = 'valider', command = saisie,width=5)
bout.config(fg='blue',bg='VioletRed2')                            #Bouton pour exécuter la fonction saisie()
bout.config(font=('verdana',10))
bout.pack()




boutouv = Button(decoder, image=photo2,command=file)              #Bouton pour exécuter la fonction file()
boutouv.config(width=90,height=60)
boutouv.pack(pady=10)





bouton3=Button(decoder, text='Quitter', command = decoder.destroy,width=5,height=1)
bouton3.config(fg='blue',bg='VioletRed2')                         #Bouton pour quitter l'interface
bouton3.config(font=('verdana',12))
bouton3.place(x='450',y='500')




decoder.mainloop()


try:
    inverse(nom,filI,fil)                                       #L'essai de l'exécution de la fonction inverse() avec affichage des messages 
    encoder=Tk()                                                #selon l'entier retourné par cette fonction (opération réussie ou attention)
    encoder.geometry("0x0+560+430")
    messagebox.showinfo('Decodage réussi',"L'image est decodée avec succès" )
    encoder.destroy()
    encoder.mainloop()

except:


    decoder=Tk()
    decoder.geometry("0x0+560+430")

    messagebox.showwarning("Warning","Aucune image n'est decodée")

    
    decoder.destroy()
    decoder.mainloop()
    
    sys.exit(1)
    
    
