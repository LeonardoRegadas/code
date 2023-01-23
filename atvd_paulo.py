class Formas_Geometricas(): 
    pass

class Triangulo(Formas_Geometricas):
    def _init_(self,base,altura):
        self.base=base 
        self.altura=altura 
  
    def get_area(self): 
        return self.base*self.altura 
    
    def set_area(self,nova_base,nova_altura): 
        self.base=nova_base 
        self.altura=nova_altura 
    
    def _str_(self): 
        return f'A area deste {self._class.name_} é {self.get_area()}'


