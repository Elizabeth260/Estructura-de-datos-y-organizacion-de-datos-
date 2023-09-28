class Cafeteria:
    def __init__(self):
        self.Alumnos = ["Alejandra","Monica","David","Alexa"]
        self.Comidas = ["Tortas", "Gorditas","Enchiladas","Empanadas"]        
        self.Bebidas = ["Cocacola","Sprite","Mirinda","Toronja"]
        self.Precios = [30,45,60,100]
        
    def agregarAlumno(self): 
        if len(self.Alumnos) < 5:
            a = input("Ingresa al nombre del Alumno: ")
            self.Alumnos.append(a)
        else:
            print("Lista llena")
            
    def asigBebida(self):
        for Alumno,Comida,Precio,Bebida in zip(self.Alumnos, self.Comidas, self.Precios, self.Bebidas):
            print(f"Alumno {Alumno} pago de la comida {Comida} de ${Precio} y tiene la bebida {Bebida}")
            
    def Ordenar(self):
        for f in range(len(self.Precios)-1):
            if self.Precios[f] > self.Precios[f+1]:
                self.Precios[f], self.Precios[f+1] = self.Precios[f+1], self.Precios[f]
                
    def darPrecios(self):
        for Comida, Precio in zip(self.Comidas, self.Precios):
            print(f"{Comida} cuestan ${Precio}")
