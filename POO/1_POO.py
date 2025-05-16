class Perro:
    # constructor: es el que construye la clase
    def __init__(self, name, breed, collor):
        self.tamano = None
        self.edad = 0
        self.color = collor
        self.raza = breed
        self.nombre = name

    # metodos
    def ladrar(self):
        print("{} esta ladrando.".format(self.nombre))
    
    def comer(self):
        print("{} esta comiendo.".format(self.nombre))

    def jugar(self):
        print("{} esta jugando.".format(self.nombre))
    
    # setter // getter
    def cambiar_nombre(self, nombre):
        self.nombre = nombre
        print("El perro ahora se llama {}".format(nombre))

    def set_edad(self, edad):
        self.edad = edad
        print("{} ahora tiene {} años".format(self.nombre, self.edad))

    def cumpleannos(self):
        self.edad += 1
        print("{} ahora tiene {} años".format(self.nombre, self.edad))

    

# Instanciar un objeto // VACIO
# mi_perro = Perro()
# print(mi_perro.nombre)
# mi_perro.comer()
# mi_perro.cambiar_nombre("Tommy")
# print(mi_perro.nombre)


# otro objeto
mi_perro2 = Perro("Kira", "Pitbul", "Negro con blanco")
print(mi_perro2.nombre)
mi_perro2.comer()

# otro objeto
mateo = Perro("Mateo", "Pinsher", "Blanco")
mateo.jugar()
mateo.set_edad(5)

