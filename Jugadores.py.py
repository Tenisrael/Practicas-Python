"""
def ingresar_jugadores():
    jugadores = []
    N = int(input("¿Cuántos jugadores quieres registrar? "))

    for i in range(N):
        nombre = input(f"\n Ingresa el nombre del jugador {i + 1}: ")
        while True:
            try:
                puntaje = int(input(f" Ingresa el puntaje de {nombre}: "))
                break
            except ValueError:
                print("\n Por favor, ingresa un número válido para el puntaje.")
        
        jugadores.append([nombre, puntaje])

    return jugadores

def mostrar_ranking(jugadores_ordenados):
    print("\n Player Ranking: ")
    for i, jugador in enumerate(jugadores_ordenados):
        print(f"{i + 1}. {jugador[0]}: {jugador[1]} puntos")

def main():
    jugadores = ingresar_jugadores()

    # Ordenar por el puntaje en orden descendente
    jugadores_ordenados = sorted(jugadores, key=lambda x: x[1], reverse=True)

    # Mostrar el ranking
    mostrar_ranking(jugadores_ordenados)

if __name__ == "__main__":
    main()
"""
"""
class Vector:
    def __init__(self):
        self.data = []
    
    def append(self, value):
        self.data.append(value)
    
    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")
    
    def size(self):
        return len(self.data)
    
    def __repr__(self):
        return str(self.data)

class PlayersScores:
    def __init__(self):
        self.playerNames = Vector()
        self.scores = Vector()
    
    def add_player(self, name, score):
        self.playerNames.append(name)
        self.scores.append(score)
    
    def get_score(self, name):
        for i in range(self.playerNames.size()):
            if self.playerNames.get(i) == name:
                return self.scores.get(i)
        return None
    
    def display_scores(self):
        for i in range(self.playerNames.size()):
            print(f"{self.playerNames.get(i)}: {self.scores.get(i)}")

# Función principal interactiva
def main():
    players_scores = PlayersScores()
    
    while True:
        print("\nOpciones:")
        print("1. Añadir jugador y puntaje")
        print("2. Mostrar todos los puntajes")
        print("3. Obtener el puntaje de un jugador específico")
        print("4. Salir")
        
        choice = input("Selecciona una opción: ")
        
        if choice == "1":
            name = input("Introduce el nombre del jugador: ")
            score = int(input("Introduce el puntaje del jugador: "))
            players_scores.add_player(name, score)
            print(f"Jugador {name} con puntaje {score} ha sido añadido.")
        
        elif choice == "2":
            print("\nPuntajes de los jugadores:")
            players_scores.display_scores()
        
        elif choice == "3":
            name = input("Introduce el nombre del jugador: ")
            score = players_scores.get_score(name)
            if score is not None:
                print(f"Puntaje de {name}: {score}")
            else:
                print(f"El jugador {name} no fue encontrado.")
        
        elif choice == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
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
