"""
class Vector:
    def _init_(self):
        self.datos = []
        self.N = 0

    def leer_vec(self, N):
        self.N = N
        self.datos = []
        print(f"Ingrese {N} datos para el Vector:")
        for i in range(N):
            dato = input(f"Dato {i+1}: ")
            self.datos.append(dato)
        return self.datos

    def imprimir_vec(self):
        if not self.esta_lleno():
            print("Error: El Vector debe estar lleno antes de imprimir.")
            return
        print("Contenido del Vector:")
        for i, dato in enumerate(self.datos):
            print(f"Dato {i+1}: {dato}")

    def esta_vacio(self):
        return len(self.datos) == 0

    def esta_lleno(self):
        return len(self.datos) == self.N

#------------------- VALIDACION -------------------#

def validar (tipo,mensaje):
    while True:
        try:
            valor = tipo(input(mensaje))
        except ValueError:
            print("\n ¡ERROR! debe ingresar un número  \n")    
        else:
            break
    return valor

# Ejemplo de uso
vector = Vector()

# Leer vector
N = validar(int,"Ingresa el número de jugadores: ")
vector.leer_vec(N)

# Imprimir vector
vector.imprimir_vec()
"""

"""
# Definir la función para registrar jugadores y puntajes
def registrar_jugadores():
    # Pedir el número de jugadores
    n = int(input("Ingrese el número de jugadores: "))

    # Inicializar listas para nombres y puntajes
    nombres = []
    puntajes = []

    # Registrar jugadores y puntajes
    for i in range(n):
        nombres.append(input(f"\n Ingrese el nombre del jugador {i+1}: "))
        puntajes.append(int(input(f" Ingrese el puntaje del jugador {i+1}: ")))

    # Mostrar los resultados
    print("\n * * * Lista de jugadores y puntajes * * * ")
    for i in range(n):
        print(f"{nombres[i]}: {puntajes[i]}")

# Llamar a la función para registrar jugadores
registrar_jugadores()
"""

"""
# Definir la función para registrar jugadores y puntajes
def registrar_jugadores():
    # Pedir el número de jugadores
    n = int(input("Ingrese el número de jugadores: "))

    # Inicializar listas para nombres y puntajes
    nombres = []
    puntajes = []

    # Registrar jugadores y puntajes
    for i in range(n):
        nombres.append(input(f"\n Ingrese el nombre del jugador {i+1}: "))
        puntajes.append(int(input(f" Ingrese el puntaje del jugador {i+1}: ")))

    # Ordenar los resultados de mayor a menor
    lista_ordenada = sorted(zip(puntajes, nombres), reverse=True)

    # Mostrar los resultados
    print("\n * * * Lista de jugadores y puntajes ordenada de mayor a menor * * * ")
    for puntaje, nombre in lista_ordenada:
        print(f" { nombre } : { puntaje }")

# Llamar a la función para registrar jugadores
registrar_jugadores()

"""
"""
# Definir la función para registrar jugadores y puntajes
def registrar_jugadores():
    # Pedir el número de jugadores
    n = int(input("Ingrese el número de jugadores: "))

    # Inicializar listas para nombres y puntajes
    nombres = []
    puntajes = []

    # Registrar jugadores y puntajes
    for i in range(n):
        nombres.append(input(f"\nIngrese el nombre del jugador {i + 1}: "))
        while True:
            try:
                puntaje = int(input(f"Ingrese el puntaje del jugador {i + 1}: "))
                puntajes.append(puntaje)
                break
            except ValueError:
                print("Por favor, ingrese un número válido para el puntaje.")

    # Ordenar los resultados de mayor a menor
    lista_ordenada = sorted(zip(puntajes, nombres), reverse=True)

    # Mostrar los resultados
    print("\n* * * Lista de jugadores y puntajes ordenada de mayor a menor * * *")
    print("| Nombre     |    Puntaje   |")
    print("|-----------------------------|")
    for puntaje, nombre in lista_ordenada:
        print(f" {nombre:<10} | {puntaje:>10}")

# Llamar a la función para registrar jugadores
registrar_jugadores()
"""

class SistemaDeJugadores:
    def __init__(self):
        # Inicializar listas para nombres y puntajes
        self.nombres = []
        self.puntajes = []

    def registrar_jugador(self, nombre, puntaje):
        """
        Registra un jugador con su nombre y puntaje.
        """
        self.nombres.append(nombre)
        self.puntajes.append(puntaje)

    def obtener_resultados_ordenados(self):
        """
        Devuelve una lista de tuplas con los jugadores y sus puntajes ordenados de mayor a menor.
        """
        # Ordenar por puntajes de mayor a menor
        return sorted(zip(self.puntajes, self.nombres), reverse=True)

    def mostrar_resultados(self):
        """
        Muestra los resultados ordenados en la consola.
        """
        print("\n * * * Lista de jugadores y puntajes ordenada de mayor a menor * * * ")
        lista_ordenada = self.obtener_resultados_ordenados()
        for puntaje, nombre in lista_ordenada:
            print(f" {nombre} : {puntaje}")


# Ejemplo de uso
sistema = SistemaDeJugadores()

# Registrar jugadores
n = int(input("Ingrese el número de jugadores: "))
for i in range(n):
    nombre = input(f"\n Ingrese el nombre del jugador {i+1}: ")
    puntaje = int(input(f" Ingrese el puntaje del jugador {i+1}: "))
    sistema.registrar_jugador(nombre, puntaje)

# Mostrar resultados
sistema.mostrar_resultados()
