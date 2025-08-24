# chakana_memoria_ancestral.py
# Juego de preguntas tipo trivia inspirado en la Chakana y el conocimiento ancestral.

import random

class Colores:
    RESET = "\033[0m"
    AZUL = "\033[94m"
    AMARILLO = "\033[93m"
    ROJO = "\033[91m"
    VERDE = "\033[92m"

def bienvenida():
    print(Colores.AZUL + "\n☀️ Bienvenido al Despertar de la Memoria Ancestral ☀️" + Colores.RESET)
    print("\nEste juego se basa en conocimientos vinculados con la Chakana, el equilibrio, la vida en comunidad y los saberes andinos.")
    nombre = input("\nEscribe tu nombre ancestral: ")
    return nombre

preguntas = [
    {
        "pregunta": "¿Qué forma tiene la chakana tradicional?",
        "opciones": ["a) Círculo", "b) Espiral", "c) Cruz escalonada", "d) Estrella"],
        "respuesta": "c"
    },
    {
        "pregunta": "¿Qué elemento natural se asocia con el Hanan Pacha?",
        "opciones": ["a) Agua", "b) Aire", "c) Tierra", "d) Fuego"],
        "respuesta": "b"
    },
    {
        "pregunta": "¿Cuál es un valor clave en la cosmovisión andina?",
        "opciones": ["a) Competencia", "b) Individualismo", "c) Dualidad y reciprocidad", "d) Explotación"],
        "respuesta": "c"
    }
]

def jugar(nombre):
    puntos = 0
    random.shuffle(preguntas)
    for p in preguntas:
        print(Colores.AMARILLO + "\n" + p["pregunta"] + Colores.RESET)
        for o in p["opciones"]:
            print(o)
        r = input("Tu respuesta: ").lower()
        if r == p["respuesta"]:
            print(Colores.VERDE + "✔️ Correcto!" + Colores.RESET)
            puntos += 1
        else:
            print(Colores.ROJO + f"✖️ Incorrecto. La respuesta correcta era '{p['respuesta']}'." + Colores.RESET)
    return puntos

def final(nombre, puntos):
    print(Colores.AZUL + f"\nGracias por jugar, {nombre}. Obtuviste {puntos}/{len(preguntas)} puntos." + Colores.RESET)
    if puntos == len(preguntas):
        print("🌟 ¡Sabio ancestral! Has conectado con la sabiduría de los abuelos.")
    elif puntos >= 2:
        print("🌿 Buen camino. Tu memoria ancestral está floreciendo.")
    else:
        print("🌒 Aún hay mucho por recordar. Escucha a la tierra.")

def main():
    nombre = bienvenida()
    puntos = jugar(nombre)
    final(nombre, puntos)

if __name__ == "__main__":
    main()
