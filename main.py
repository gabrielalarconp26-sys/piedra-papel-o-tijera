import random


class Hand:
    def __init__(self, choice):
        if choice not in {"piedra", "papel", "tijera"}:
            raise ValueError("La hand debe ser 'piedra', 'papel' o 'tijera'")
        self.hand = choice
        
# funciones necesarias
def whoWon(user_hand, machine_hand):
    if user_hand == machine_hand:
        print(">empate")
    elif(
        (user_hand == "piedra" and machine_hand == "tijera")
        or
        (user_hand == "papel" and machine_hand == "piedra")
        or
        (user_hand == "tijera" and machine_hand == "papel")
        ):
        print(">machine: Tú ganas...")
    else:
        print(">machine: Yo gano, ja ja...")

def revancha():
    opcion = str(input("respuesta del usuario: ")).lower()
    while True:
        if opcion not in {"si", "sí", "ok", "ya", "dale", "vale", "yes", "s", "y", "no", "nop", "adios", "n", "bye"}:
            print("No entendí tu respuesta... ")
            opcion = str(input("respuesta del usuario: "))
            continue
        elif opcion in {"si", "sí", "ok", "ya", "dale", "vale", "yes", "s", "y"}:
            return True
        else:
            print(">machiene: Adiós")
            return False

# correr juego

while True:
    choice = str(input("Indique su elección: 'piedra', 'papel' o 'tijera': "))
    if choice in {"piedra", "papel", "tijera"}:
        my_hand = Hand(choice)
        print(">machine: su mano es", my_hand.hand)
        machine_choice = random.choice(["piedra", "papel", "tijera"])
        machine = Hand(machine_choice)
        print(">machine: mi mano es", machine.hand)
        whoWon(my_hand.hand, machine.hand)
        print("¿Quieres jugar otra vez?")
        if revancha():
            continue
        else:
            break

    else:
        print("Debe elegir una entre 'piedra', 'papel' o 'tijera'")