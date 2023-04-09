class Agente:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.padre = None
        self.maxx = None
        self.maxy = None
        self.xob = None
        self.yob = None
        
    def arriba(self):
        aux = self.posx - 1
        if aux >= 0:
            self.posx = aux
            return True
        return False
    def izquierda(self):
        aux = self.posy - 1
        if aux >= 0:
            self.posy = aux
            return True
        return False
    
    def abajo(self):
        aux = self.posx + 1
        if aux < self.maxx:
            self.posx = aux
            return True
        return False
    def derecha(self):
        aux = self.posy + 1
        if aux < self.maxy:
            self.posy = aux
            return True
        return False
    
    def es_funcion_objetivo(self):
        if self.posx == self.xob and self.posy == self.yob:
            return True
        return False