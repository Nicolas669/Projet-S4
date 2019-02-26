#BOUHENTALA Younes
#22/03/17
#Projet Huffman




from copy import copy
"""paires objet de la class point"""
#classe des paires du plan

class Paire():
    """classes des paires"""
    def __init__(self,a,b):
        """x et y sont des attributs"""
        self.element = a
        self.priorite = b


    def afficherpaire(self):
        """afficher est une fonction observatrice"""
        print(self.element)
        print(self.priorite)


    def translater(self,a,b):
        self.element = self.element + a
        self.priorite=self.priorite + b


    def getPriorite(self):
        return self.priorite


    def getElement(self):
        return self.element


    def setElement(self,a):
        self.element=a


    def setPriorite(self,b):
        self.priorite=b


    def eqPaire(self,p2):
        return self.getElement() == p2.getElement() and self.getPriorite() == p2.getPriorite()
        """renvoie True si les deux paires sont égales, False sinon"""





#classes filePrio
class filePrio():
    """classes des filed'attentes"""
    def __init__(self, a):
        self.filePrio=a


    def estVide(self):
        assert not( self.filePrio==[[],[]])


    def teteFilePrio(self):
        assert self.estVide()== True
        return self.filePrio[0]


    def queueFileprio(self):
        assert self.estVide()==True
        return self.filePrio[-1]

    def ajoutFileprio(self,paire):
        assert self.estVide()==True
        z=0
        while self.filePrio[z][1].getPriorite()>paire.getPriorite() and z<len(self.filePrio):
                z=z+1
        self.filePrio=self.filePrio.insert(z,paire)

    def afficherfile(self):
        for i in self.filePrio:
            print(i.afficherpaire())
        """afficher la file d'attente"""



class Noeud():
    """la classe Noeuds representant les noeuds de l'arbre"""
    def __init__(self):
        self.Noeud = None


    def getVal(self):
        """la methode getval revoie la valeur du noeud"""
        return self.Noeud


    def setVal(self,val):
        """la methode setval donne une valeur à ce noeud"""
        self.Noeud= val





class Arbre():
    """la classe arbre avec le constructeur qui construit l'rbre vide"""
    def __init__(self):
        self.fd = None
        self.fg  = None
        self.racine = None


    def getFd(self):
        """renvoie le fils droit de l’arbre
                Precondition: arbre non vide"""
        assert (not self.estVide())
        return self.fd


    def getFg(self):
        """renvoie le fils gauche de l’arbre
                Precondition: arbre non vide"""
        assert (not self.estVide())
        return self.fd



    def estVide(self):
        return self.racine is None and self.getFg() is None and self.getFd() is None
    """Les fonctions racine, fg, fd deviennent des getter getRac, getFg, getFd"""



    def getRac(self):
        """renvoie la racine de l’arbre
        Precondition: arbre non vide"""
        assert (not self.estVide())
        return self.racine.getVal()


    def estFeuille(self):
        """ renvoie True ssi l’arbre se reduit à une feuille"""
        return self.getFd().estVide() and self.getFg().estVide()
    """Une autre version autorisant l’arbre vide"""

    def hauteur(self):
        """renvoie la hauteur maximal de l'arbre"""
        if self.estVide() or self.estFeuille():
            return 0

        else:
         return 1 + max(self.getFd().hauteur(), self.getFg().hauteur())



    def creerArbre(self,A1,N,A2):
        self.fd= A2
        self.fg= A1
        self.racine= N

    def préfixe(self):
        if not self.estVide():
            """ afficher d'abord la racines puis les noeuds du files gauche puis ceux du droit """
            self.getRac().afficher()
            self.getFg().préfixe()
            self.getFd().préfixe()


    def suffixe(self):
        if not self.estVide():
            """ afficher d'abord les feuilles puis les racines"""
            self.getFg().suffixe()
            self.getFd().suffixe()
            self.getRac().afficher()


    def inffixe(self):
        """"afficher l'arbres des manieres roulot compresseur et permet de l'es ordonner de manieres expression algebrique"""
        if not self.estVide():
            self.getFg().inffixe()
            self.getRac().afficher()
            self.getFd().inffixe()


    def evalue(self):

            if not(self.estFeuille()):
                if self.getRac().getVal=='*':
                    return self.getFg().evalue()*self.getFd().evalue()
                else:
                    return self.getFg().evalue()+self.getFd().evalue()
            else: return self.getRac().getVal()


    def setFg(self,A1):
        self.fg=A1


    def setFd(self,A2):
        self.fd=A2

    def setRacine(self,N):
        self.racine=N
