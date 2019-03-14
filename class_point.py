

class Point:

    def __init__(self, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def getAbscisse(self):
        """ None --> float """
        return self.abscisse

    def getOrdonnee(self):
        """ None --> float """
        return self.ordonnee

    def setAbscisse(self, value):
        """ float --> None """
        assert isinstance(value, float)
        self.abscisse = value

    def setOrdonnee(self, value):
        """ float --> None """
        assert isinstance(value, float)
        self.ordonnee = value

    def __eq__(self, other):
        """ Point --> Bool """
        assert isinstance(other, Point)
        return self.getAbscisse() == other.getAbscisse() and self.getOrdonnee() == other.getOrdonnee()

    def milieu(self, other):
        """ Point --> Point
         Donne le milieu du segment [self, other] """
        assert isinstance(other, Point)
        x = (self.getAbscisse() + other.getAbscisse())/2
        y = (self.getOrdonnee() + other.getOrdonnee())/2
        return Point(x, y)
    
    def __str__(self):
        x, y = self.getAbscisse(), self.getOrdonnee()
        return "Point({},{})".format(x, y)
