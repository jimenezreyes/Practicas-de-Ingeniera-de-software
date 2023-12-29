"""
Author: Jimenez Reyes Abraham
"""

class JuegoTenis:
    def __init__(self):
        # Inicializamos valores (jugadores y puntajes)
        self.jugador1 = input("Ingresa el nombre del Jugador 1: ")
        self.jugador2 = input("Ingresa el nombre del Jugador 2: ")
        self.sets_jugador1 = 0
        self.sets_jugador2 = 0
        self.juegos_jugador1 = 0
        self.juegos_jugador2 = 0
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0
        self.cambio_lado = False
        self.juego_terminado = False

    def punto_anotado(self, jugador):

        #Verificamos si el juego ha terminado antes de anotar un punto
        if self.juego_terminado:
            print("El juego ha terminado. No se pueden anotar más puntos.")
            return
        #Se le asigna un punto a un jugador
        if jugador == self.jugador1:
            self.puntos_jugador1 += 1
        elif jugador == self.jugador2:
            self.puntos_jugador2 += 1
        else:
            print("Jugador desconocido. Inténtalo de nuevo. \n")
            return
        #Verificamos si se ha ganado un set
        self.verificar_ganador_set()


    def verificar_ganador_set(self):
        #Verificamos quien ha ganado el set o si hay empate
        if self.puntos_jugador1 >= 4 and self.puntos_jugador1 - self.puntos_jugador2 >= 2:
            self.ganar_set(self.jugador1)
        elif self.puntos_jugador2 >= 4 and self.puntos_jugador2 - self.puntos_jugador1 >= 2:
            self.ganar_set(self.jugador2)
        elif self.puntos_jugador1 >= 3 and self.puntos_jugador2 >= 3:
            if self.puntos_jugador1 == self.puntos_jugador2:
                print("Iguales, se juega el desempate ")
            elif self.puntos_jugador1 > self.puntos_jugador2:
                print(f"Ventaja para {self.jugador1}")
            else:
                print(f"Ventaja para {self.jugador2}")
        else:
            self.mostrar_puntaje()


    def ganar_set(self, ganador):
        # Ganador de un set y actualizamos los puntajes
        print(f"{ganador} ha ganado el set! \n")
        if ganador == self.jugador1:
            self.sets_jugador1 += 1
        else:
            self.sets_jugador2 += 1

        # Reiniciamos los puntajes para el siguiente set
        self.juegos_jugador1 = 0
        self.juegos_jugador2 = 0
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0

        # Verificamos si se ha ganado el juego
        if self.sets_jugador1 == 3:
            self.mostrar_ganador_partido(self.jugador1)
            self.juego_terminado = True
        elif self.sets_jugador2 == 3:
            self.mostrar_ganador_partido(self.jugador2)
            self.juego_terminado = True
        else:
            self.cambio_lado = True  
            print("Cambio de lado \n")  


    def mostrar_puntaje(self):
        # Puntaje actual 
        print(f"Puntaje: {self.jugador1} {self.puntos_jugador1} - {self.puntos_jugador2} {self.jugador2}")

    def mostrar_ganador_partido(self, ganador):
        # Ganador del juego
        print(f"¡{ganador} ha ganado el partido! \n")

    def jugar(self):
        """
        Mientras el juego no termine, ejecutamos el juego que 
        permite anotar puntos hasta ganar los 3 sets
        """
        while not self.juego_terminado:
            while self.sets_jugador1 < 3 and self.sets_jugador2 < 3:
                jugador = input("¿Quién anotó un punto? (Ingresa el nombre del jugador): ")
                self.punto_anotado(jugador)

            if self.sets_jugador1 == 3:
                self.mostrar_ganador_partido(self.jugador1)
            elif self.sets_jugador2 == 3:
                self.mostrar_ganador_partido(self.jugador2)

            decision = input(" ¿Quieres jugar otra vez? (s/n): ")
            if decision.lower() == 'n':
                self.juego_terminado = True
            else:
                self.reiniciar_juego()

    def reiniciar_juego(self):
        # Reiniciamos todos los valores del juego para una nueva partida.
        self.sets_jugador1 = 0
        self.sets_jugador2 = 0
        self.juegos_jugador1 = 0
        self.juegos_jugador2 = 0
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0
        self.cambio_lado = False
        self.juego_terminado = False

if __name__ == "__main__":
    juego = JuegoTenis()
    juego.jugar()