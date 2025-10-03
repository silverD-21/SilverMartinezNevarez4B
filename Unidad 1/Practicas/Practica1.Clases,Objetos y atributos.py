#Practica 1 Clases, objetos y atributos

#Una clase es una plantilla o un molde que define como será un objeto
class Persona:
    def _init_ (self, nombre, edad): #Constructor de una clase
        self.nombre = nombre
        self.edad = edad 
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad +=1 
        print(f"Esta persona cumplió: {self.edad}")

#Un objeto es una instancia creada a partir de una clase
#Crear objeto que pertenece a una clase
estudiante1 = Persona("Helena", 19)
estudiante2 = Persona("Silver", 19)

#Asignar métodos  esos objetos (Acciones)
estudiante1.presentarse()
estudiante1.cumplir_anios()

# Paso 1. Agrega un método cumplir_anios() que aumente en 1 la edad

#INSTANCIA:
#Cada objeto creado de una clase es una instancia
#Podemos tener varias instancias que coexistan con sus propios datos
#Objeto = instancia de la clase.
#Cada vez que se crea un objeto con Clase() se obtiene una instancia dependiente.
#Cada instancia tiene sus propios datos aunque vengan de la misma clase.

#Abstracción
# Representr solo lo importante del mundo real, ocultando detalles inecesarios.

class automovil:
    def _init_(self, marca):
        self.marca = marca

    def arrancar(self):
        print(f"{self.marca} arrancó")

#Crear un objeto y asignar una marca
auto = automovil("BMW")
auto.arrancar()

#Abstracción: Nos centramos solo en los que importa (accion) que es arrancar el automovil, ocultando 
# detalles internos como motor, transmisión, tipo_combustible.
#Enfoque solo en la acción del objeto.
#Objetivo es hacer el codigo mas limpio y fácil de usar.

# Practica 1.2
#1. Crear una clase mascotas
#2. agregar minimo 4 atributos 
#3. Definir al menos 4 métodos diferentes.
#4. Crear 2 instancias de la clase
#5. Llamar los métodos y aplicar abstracción. (Agregar un atributo innecesario)

class mascotas:
    def _init_(self, nombre, animal, raza, anios, peso):
        self.animal = animal
        self.raza = raza
        self.anios = anios
        self.nombre = nombre
        self.peso = peso

    def presentar(self):
        print(f"Hola mi nombre es {self.nombre}")

    def sonido_animal(self):
        if self.animal == "perro":
            print(f"El sonido que hago es guau guau")
        elif self.animal == "gato":
            print(f"El sonido que hago es miau miau")
        else:
            print("Sonido desconocido")

    def tipo_raza (self):
        print(f"Soy un {self.raza}")

    def cumplir_anios (self):
        self.anios +=1 
        print(f"Este año cumplo {self.anios} años")

mascota1 = mascotas("Maya", "perro", "Schnauzer", 6)
mascota2 = mascotas("Kira", "gato", "Siamés", 4)

mascota1.presentar()
mascota1.sonido_animal()
mascota1.tipo_raza()
mascota1.cumplir_anios()

mascota2.presentar()
mascota2.sonido_animal()
mascota2.tipo_raza()
mascota2.cumplir_anios()