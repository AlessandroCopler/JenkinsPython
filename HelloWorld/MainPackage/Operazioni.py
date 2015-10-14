

class Operazioni(object):

    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def somma(self):
        return self.a+self.b
    
    def differenza(self):
        if(self.a>self.b):
            return self.a-self.b
        return 0
    
    def prodotto(self):
        return self.a*self.b
    
    def divisione(self):
        return int(self.a/self.b)