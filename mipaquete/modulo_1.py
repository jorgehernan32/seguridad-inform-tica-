def jugar_piedra_papel_tijera():
    opciones = ["piedra", "papel", "tijera"]

    print("¡Bienvenido al juego de Piedra, Papel o Tijera!")
    print("Las opciones son: piedra, papel, tijera.")

    while True:
        jugador = input("Elige una opción (piedra, papel o tijera), o 'q' para salir: ").lower()

        if jugador == 'q':
            print("¡Gracias por jugar!")
            break
        elif jugador not in opciones:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        computadora = random.choice(opciones)
        print(f"La computadora elige: {computadora}")

        if jugador == computadora:
            print("Empate.")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra"):
            print("¡Ganaste!")
        elif (jugador == "tijera" and computadora == "papel"):
            print("¡Ganaste!")
        else:
            print("¡Perdiste!")

if __name__ == "__main__":
    jugar_piedra_papel_tijera()
