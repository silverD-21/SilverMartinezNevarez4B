#Practica 4 Herencia

class Ticket:
    def __init__ (self, id, prioridad, tipo):
        self.id = id
        self.prioridad = prioridad
        self.tipo = tipo
        self.estado = "Pendiente"
    
    def identificar(self):
        print()

class Empleado:
    def __init__ (self, nombre ):
        self.nombre = nombre

    def trabajar_ticket(self):
        print(f"El empleado {self.nombre} esta trabajando en ticket {self.id}")


class Desarrollador(Empleado):
    def trabajar_ticket(self, ticket):
        if ticket.tipo =="Software":
            ticket.estado =="Resuelto"
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print(f"El desarrollador {self.nombre} no puede resolver este tipo de ticket")




class Tester(Empleado):
        def trabajar_ticket(self, ticket):
            if ticket.tipo =="Prueba":
                ticket.estado =="Resuelto"
                print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
            else:
                print(f"El desarrollador {self.nombre} no puede resolver este tipo de ticket")

class Proyect_Manager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print (f"{self.nombre} asigno el ticket {ticket.id}, a el empleado {empleado.nombre}")
        empleado.trabajar_ticket(ticket)

#Crea tickets y empleados (Instancias de objetos)
ticket1 = Ticket (1, "alta", "Software")
ticket2 = Ticket (2, "media", "Prueba")


developer1 = Desarrollador ("Gustavo")
tester1 = Desarrollador ("Pablo")
pm1 = Proyect_Manager ("Susana")

pm1.asignar_ticket(ticket1, developer1)

#Parte adicional
#Agregar un menu con while y con if que permita:
#1. Crear ticket
#2. Ver ticket
#3. Asignar tickets
#4. Salir programa