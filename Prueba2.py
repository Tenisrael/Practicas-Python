# Función para ingresar los datos de los jugadores
def ingresar_jugadores():
    # Inicializa una lista vacía para almacenar los datos de los jugadores
    jugadores = []
    
    # Solicita al usuario el número de jugadores que quiere registrar
    N = int(input("¿Cuántos jugadores quieres registrar? "))

    # Bucle para ingresar el nombre y puntaje de cada jugador
    for i in range(N):
        # Solicita el nombre del jugador
        nombre = input(f"\nIngresa el nombre del jugador {i + 1}: ")

        # Bucle para asegurar que se ingrese un puntaje válido
        while True:
            try:
                # Solicita el puntaje del jugador y verifica que sea un número entero
                puntaje = int(input(f"Ingresa el puntaje de {nombre}: "))
                break  # Sale del bucle si el puntaje es válido
            except ValueError:
                # Muestra un mensaje de error si se ingresa un valor no numérico
                print("Por favor, ingresa un número válido para el puntaje.")
        
        # Añade el nombre y puntaje del jugador a la lista
        jugadores.append([nombre, puntaje])

    # Devuelve la lista de jugadores con sus puntajes
    return jugadores

# Función para mostrar el ranking de los jugadores
def mostrar_ranking(jugadores_ordenados):
    print("\nPlayer Ranking:")
    # Bucle para mostrar cada jugador en el ranking
    for i, jugador in enumerate(jugadores_ordenados):
        # Muestra la posición en el ranking, el nombre del jugador y su puntaje
        print(f"{i + 1}. {jugador[0]}: {jugador[1]} puntos")

# Función principal del programa
def main():
    # Llama a la función para ingresar los datos de los jugadores
    jugadores = ingresar_jugadores()

    # Ordena la lista de jugadores por puntaje en orden descendente
    jugadores_ordenados = sorted(jugadores, key=lambda x: x[1], reverse=True)

    # Llama a la función para mostrar el ranking de los jugadores
    mostrar_ranking(jugadores_ordenados)

# Verifica si el script está siendo ejecutado directamente
if __name__ == "__main__":
    main()
