#super class
class Rectangle() :
    __NbR = 0
    def __init__(self, largeur, longueur) :
        self.__largeur = largeur
        self.__longueur = longueur
        Rectangle.__NbR = Rectangle.__NbR + 1

#getters and setters 
    def getlargeur(self) :
        return self.__largeur
    
    def getlongueur(self) :
        return self.__longueur
    
    def getNmB(self) :
        return Rectangle.__NbR
    
    def setlargeur(self, largeur) :
        self.__largeur = largeur

    def setlongueur(self, longueur) :
        self.__longueur = longueur

#methodes
    def perimetre(self) :
        return (self.getlargeur() + self.getlongueur())*2
    
    def surface(self) :
        return (self.getlargeur() * self.getlongueur())
    
    def ToString(self) :
        return ("le longueur est :", self.getlongueur(), "le largeur est : ", self.getlargeur())
    
    def equals(self, R) :
        lon1, lar1 = self.getlongueur(), self.getlargeur()
        lon2, lar2 = Rectangle.getlongueur(), Rectangle.getlargeur()
        if lon1 == lon2 and lar1 == lar2 :
            return True
        else : 
            return False
        
#subclass
class parallelepipede(Rectangle) :
    __NbP = 0
    def __init__(self, largeur, longueur, hauteur):
        super().__init__(largeur, longueur)
        self.__hauteur = hauteur
        parallelepipede.__NbP = parallelepipede.__NbP + 1

#getters and setters 
    def gethauteur(self) :
        return self.__hauteur
    
    def sethauteur(self, hauteur) :
        self.__hauteur = hauteur
    
#methodes
    def surface(self):
        return 2 * (Rectangle.getlargeur * Rectangle.getlongueur + Rectangle.getlongueur * parallelepipede.gethauteur + Rectangle.getlargeur * parallelepipede.gethauteur)
    
    def volume(self) :
        return Rectangle.getlongueur * Rectangle.getlargeur * parallelepipede.gethauteur
    
    def ToString(self):
        return super().ToString(), "la hauteur est :", parallelepipede.gethauteur
    
    def equals(self):
        hau1 = self.gethauteur
        hau2 = parallelepipede.gethauteur
        if hau1 == hau2 :
          return True