class Taxi:
    def __init__(self, ID):
        self.ID = ID
        self.estado = "EN RUTA"  # Cambiado de "STOP" a "EN RUTA"
        self.pos = "1,1"
        self.autenticado = False
        self.ocupado = False
    
    def cambiar_posicion(self, nueva_pos):
        self.pos = nueva_pos
    
    def autenticar(self):
        self.autenticado = True

    def ocupar(self):
        self.ocupado = True

    def __str__(self):
        return (f"Taxi {self.ID}:\n"
                f"  Estado: {self.estado}\n"
                f"  Posición: {self.pos}\n"
                f"  Autenticado: {'Sí' if self.autenticado else 'No'}\n"
                f"  Ocupado: {'Sí' if self.ocupado else 'No'}\n"
                f"----------------------")


def generar_taxis(num_taxis):
    if num_taxis <= 0:
        print("El número de taxis debe ser mayor a 0.")
        return

    for i in range(1, num_taxis + 1):
        taxi = Taxi(str(i))
        print(taxi)


if __name__ == "__main__":
    try:
        num_taxis = int(input("Introduce el número de taxis: "))
        generar_taxis(num_taxis)
    except ValueError:
        print("Por favor, introduce un número válido.")
print('Este es un fallo')
