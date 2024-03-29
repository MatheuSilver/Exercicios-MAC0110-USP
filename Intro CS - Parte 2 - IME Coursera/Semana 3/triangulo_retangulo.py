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
        tam=[self.b, self.c]
        maior = self.a
        if maior < self.b and self.b > self.c: 
            maior = self.b
            tam[0]=self.a
        elif maior < self.c and self.c > self.b: 
            maior = self.c
            tam[1] = self.a

        print(tam)
        print(maior)

        return maior**2 == tam[0]**2+tam[1]**2