from tkinter import * #  importe tous les éléments du module Tkinter
import time 

fenetre = Tk() #crée une interface de la classe Tk, qui représente la fenêtre principale 

large_fen =4*fenetre.winfo_screenwidth()//4 #calculent la largeur et la hauteur de la fenêtre en prenant un quart de la largeur et de la hauteur de l'écran            
haut_fen = 4*fenetre.winfo_screenheight()//4 #winfo_screenwidth() et winfo_screenheight() sont des méthodes qui renvoient les dimensions de l'écran                   
fenetre.geometry(str(large_fen)+'x'+str(haut_fen))#définit la géométrie de la fenêtre en utilisant la méthode geometry et ajuste ainsi la taille de la fenêtre principale
cadre = Canvas(fenetre,
                 bg= 'white',width = large_fen,height = haut_fen,highlightthickness = 0)
#Cette ligne crée un objet Canvas à l'intérieur de la fenêtre 
#Définie la couleur de fond, la largeur et la hauteur du canevas
#highlightthickness=0 désactive la bordure du canvas            


class Pile:
    """ classe pile permettant de pouvoir de creer et modifier nos piles issus de différentes class"""

    def __init__(self):
        self.valeurs  = []

        """ initialisation d'une nouvelle pile vide"""

    def empiler(self,valeur):
        self.valeurs.append(valeur)
        """ empile une valeur à une pile """

    def depiler(self):
        if self.valeurs:
            return self.valeurs.pop()
        """ depile le dernier element de la pile"""

    def estVide(self):
        return self.valeurs == []

    """ vérifie si la pile est vide """
    
	    

    



class Tour:
    """ Classe Tour qui permet la creation des modules baton, disques et insérer les coordonnées nécessaires"""

    def __init__(self,cadre):
        """ initialise les différentes piles pour chaque tour et prend de nouvelles coordonnées, creer une pile de 15 disques sur tour gauche"""
        self.pile_gauche = Pile()#crée une instance de la classe Pile et l'assigne à l'attribut pile_gauche
        for i in range(0,15):
            self.pile_gauche.empiler(i)#crée une pile de 15 disques sur la tour gauche
        self.pile_milieu = Pile()#crée une instance vide de la classe Pile et assigne a l'attribut pile_milieu
        self.pile_droite = Pile()#crée une instance vide de la classe Pile et assigne a l'attribut pile_droite
        self.cadre = cadre
        self.__PosX1=250#placement des tours(abscisse)
        self.__PosY1=650#placement des tours(ordonées)
        
        



    def baton(self):
        """ crée 3 batonnets afin d'y mettre les disques """
        for i in range(3):
            self.cadre.create_rectangle(self.__PosX1-7, self.__PosY1-450,self.__PosX1+7,self.__PosY1, fill='black')
            #Utilise la méthode create_rectangle pour créé un batonnet avec les coordonnées définies
            self.__PosX1 +=400
        self.__PosX1 -=1200
        
        
        



    def disque(self):
        """ fonction servant à creer des disques sur les differents baton et à mettre les elements dans des piles par la même occasion,
            prends aussi en compte la gravité """
        pile_sauvegarde = Pile()
        g=0
        while not self.pile_gauche.estVide():           
            i = self.pile_gauche.depiler()
            pile_sauvegarde.empiler(i)
            
        while not pile_sauvegarde.estVide():
            i = pile_sauvegarde.depiler()
            self.pile_gauche.empiler(i)
            self.cadre.create_rectangle(self.__PosX1-175+i*10, self.__PosY1-g*20-10,self.__PosX1+175-i*10,self.__PosY1 -g*20 +10 , fill='green', tag=str(i))
            g=g+1
        g=0
        while not self.pile_milieu.estVide():
            i = self.pile_milieu.depiler()
            pile_sauvegarde.empiler(i)
            
        while not pile_sauvegarde.estVide():
            i = pile_sauvegarde.depiler()
            self.pile_milieu.empiler(i)
            self.cadre.create_rectangle(self.__PosX1+225+i*10, self.__PosY1-g*20-10,self.__PosX1+575-i*10,self.__PosY1 -g*20 +10 , fill='green', tag=str(i))
            g=g+1
        g=0
        while not self.pile_droite.estVide():
            i = self.pile_droite.depiler()
            pile_sauvegarde.empiler(i)
        while not pile_sauvegarde.estVide():
            i = pile_sauvegarde.depiler()
            self.pile_droite.empiler(i)
            self.cadre.create_rectangle(self.__PosX1+625+i*10, self.__PosY1-g*20-10,self.__PosX1+975-i*10,self.__PosY1 -g*20 +10 , fill='green', tag=str(i))
            g=g+1
       
    
        
        
            
            
            

      

def deplacer(nb_dp, depart, arrivee, intermediaire):
    """ fonction récursive servant à deplacer les différents disques jusqu'à ce qu'il n'y en est plus à deplacer,
        nb_dp est le nombre d'élèment à déplacer qui diminue en fonction des différents tour de deplacement.
        depart correspond à la pile de gauche qui échangera les valeurs avec les différentes piles,
        arrivee correspond à la pile de droite et intermediaire à la pile du milieu."""
    
    if nb_dp != 0:
        deplacer(nb_dp-1, depart, intermediaire, arrivee)
        
        i = depart.depiler()
        arrivee.empiler(i)
        
        cadre.delete("all") # Permet de supprimer tous les élèments du cadre
        tour.baton() # Permet de recrée un baton 
        tour.disque() # Permet de recrée les disques deplacer
        
        fenetre.update() # Permet de raffraichir la page
        
        deplacer(nb_dp-1, intermediaire, arrivee, depart)
          
  

 
def jeu():
    """ Regroupent tout les affichages (les batons, et les disques). Il affiche et éxecute le déplacement des disques"""
    
    tour.baton()    
    tour.disque()
    deplacer(15,tour.pile_gauche,tour.pile_droite,tour.pile_milieu)
    fenetre.update()
    
    
   
    



       

tour = Tour(cadre) 
cadre.pack()
jeu() # On appelle la fonction jeu qui lance le déplacement des disques et leurs affichage
fenetre.mainloop() # Permet de continuer jusqu'à ce que l'utilisateur ferme la fenêtre lui même 

