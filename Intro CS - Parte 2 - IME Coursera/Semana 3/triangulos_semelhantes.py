class Triangulo:
    
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        return self.a+self.b+self.c
    
    def tipo_lado(self):
        if self.a == self.b == self.c:
            return 'equilátero'
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "isósceles"
        else:
            return "escaleno"
        
    def retangulo(self):
        tam=[self.b,self.c]
        maior = self.a
        if maior < self.b: 
            maior = self.b 
            tam[0]=self.a
        elif maior < self.c: 
            maior = self.c
            tam[1]=self.a

        return maior**2 == tam[0]**2+tam[1]**2
    
    def semelhantes(self, obj):
        if self.a > obj.a:
            return self.a%obj.a == 0 and self.b%obj.b == 0 and self.c%obj.c == 0
        else:
            return obj.a%self.a == 0 and obj.b%self.b == 0 and obj.c%self.c == 0