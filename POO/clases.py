# como crear una clase 
class Persona:
    # Constructor de la clase persona
    def __init__(self, nombre, edad):
        self.nombre = input("Ingrese su nombre: \n")
        self.edad = input("Ingrese su edad: \n")

    # Metodo de instancia para imprimir  los detalles de la persona
    def imprimir_detalle(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Creación de instancias u objetos de la clase Persona
persona1 = Persona(nombre, edad)

#persona2 = Persona("María", 25)

# Uso de metodos instancia
persona1.imprimir_detalle()
persona2.imprimir_detalle()
