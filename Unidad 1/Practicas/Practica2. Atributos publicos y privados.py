#Practica 2. Atributos publico y privados
class Persona:
    def _init_ (self, nombre, edad): #Constructor de una clase
        self.nombre = nombre
        self.edad = edad 
        self.__cuenta = None #Atributo privado
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad +=1 
        print(f"Esta persona cumplió: {self.edad}")
   
    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene una  cuenta bancaria")

    def consultar_saldo(self):
       if self.__cuenta:
            print(f"El saldo de {self.nombre} es ${self.__cuenta.mostrar_saldo()}")
       else :
           print  (f"{self.nombre} aun no tiene cuenta bancaria")



class cuenta_bancaria:

    def __init__ (self, num_cuenta, saldo):
      self.num_cuenta = num_cuenta
      self.__saldo = saldo #Atributo privado

    def mostrar_saldo(self):
        return self.__saldo 
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se deposito la cantidad de ${cantidad} a la cuenta, nuevo saldo {self.saldo}")
        else:
            print("Ingresa una cantidad valida")

    def retirar(self, retiro, saldo, cantidad):
        if retiro > 0:
          self.__saldo -= cantidad
          print(f"")



#Crear un objeto o instancia de la clase 

        
 




    
    
#Crear un objeto o instancia de la clase
persona1 = Persona("Miguel", 20)
cuenta1 = cuenta_bancaria("001", 500)

persona1.asignar_cuenta(cuenta1)
persona1.consultar_saldo()

cuenta1.depositar(200)


#Acceder a los valores de los atributos publicos
print(persona1.nombre)
print(persona1.edad)
