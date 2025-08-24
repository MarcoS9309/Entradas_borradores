
import os
import time
import random

class Colores:
    RESET = "\033[0m"
    MORADO = "\033[95m"
    VERDE = "\033[92m"
    ROJO = "\033[91m"
    AMARILLO = "\033[93m"
    CIAN = "\033[96m"

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_chakana_ascii():
    print(Colores.MORADO + '''
        █████████
        █       █
████████   █   █   ████████
        █       █
        █████████
    ''' + Colores.RESET)

def bienvenida():
    limpiar()
    print(Colores.AMARILLO + "\n🌞 Contexto cultural: El Inti Raymi ecuatoriano 🌞" + Colores.RESET)
    print("\nEl Inti Raymi es una celebración ancestral en honor al sol (Inti), que marca el solsticio de invierno en los Andes.")
    print("En Ecuador se celebra principalmente en junio en comunidades indígenas como Cañar, Saraguro, Otavalo y Cotacachi.")
    print("Durante esta fiesta se rinde homenaje al equilibrio entre los mundos: Uku Pacha (abajo), Kay Pacha (presente) y Hanan Pacha (arriba).")
    print("Este juego toma inspiración de esa cosmovisión para invitarte a un viaje simbólico por tu interior.")
    mostrar_chakana_ascii()
    print(Colores.MORADO + "╔═══════════════════════════════════════════════════════════╗")
    print("║     Viaje Sagrado por la Chakana     ║")
    print("╚══════════════════════════════════════╝" + Colores.RESET)
    print(Colores.CIAN + "Un recorrido emocional y simbólico por tus tres mundos interiores." + Colores.RESET)
    nombre = input("\nEscribe tu nombre simbólico: ")
    return nombre

preguntas = {
    "Uku Pacha": [
        {
            "pregunta": "¿Qué representa el Uku Pacha en la cosmovisión andina?",
            "opciones": ["a) Lo superficial", "b) El mundo interior, la memoria, la raíz", "c) El cielo", "d) El comercio"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué valor se asocia con el Uku Pacha?",
            "opciones": ["a) Éxito", "b) Claridad", "c) Introspección", "d) Violencia"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué animal representa el Uku Pacha?",
            "opciones": ["a) Cóndor", "b) Puma", "c) Serpiente", "d) Llama"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué es el Uku Pacha en términos de ubicación?",
            "opciones": ["a) Mundo superior", "b) Mundo inferior/subterráneo", "c) Mundo terrenal", "d) Mundo acuático"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué simboliza principalmente el Uku Pacha?",
            "opciones": ["a) Vida cotidiana", "b) Muertos y subconsciente", "c) Dioses celestiales", "d) Animales"],
            "respuesta": "b"
        }
    ],
    "Kay Pacha": [
        {
            "pregunta": "¿Qué animal representa el Kay Pacha y su sabiduría activa?",
            "opciones": ["a) Cóndor", "b) Serpiente", "c) Puma", "d) Llama"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué simboliza el Kay Pacha?",
            "opciones": ["a) Mundo espiritual", "b) El presente y la acción", "c) El caos", "d) Los astros"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿En qué reino viven los humanos según la cosmovisión andina?",
            "opciones": ["a) Hanan Pacha", "b) Uku Pacha", "c) Kay Pacha", "d) Ninguno"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué cualidades representa el puma en el Kay Pacha?",
            "opciones": ["a) Visión y claridad", "b) Valentía y ferocidad", "c) Introspección y memoria", "d) Vuelo y libertad"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué es el Kay Pacha?",
            "opciones": ["a) Mundo de arriba", "b) Mundo de aquí, terrenal", "c) Mundo de abajo", "d) Mundo espiritual solo"],
            "respuesta": "b"
        }
    ],
    "Hanan Pacha": [
        {
            "pregunta": "¿Cuál es el valor esencial del Hanan Pacha?",
            "opciones": ["a) Riqueza", "b) Claridad espiritual", "c) Fuerza física", "d) Olvido"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué símbolo natural representa el Hanan Pacha?",
            "opciones": ["a) Serpiente", "b) Puma", "c) Cóndor", "d) Jaguar"],
            "respuesta": "c"
        },
        {
            "pregunta": "¿Qué elementos celestiales pertenecen al Hanan Pacha?",
            "opciones": ["a) Tierra y raíces", "b) Sol, luna, estrellas", "c) Ríos y montañas", "d) Animales terrestres"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué dios principal está asociado con Hanan Pacha?",
            "opciones": ["a) Pachamama", "b) Inti (sol)", "c) Viracocha solo", "d) Ninguno"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Qué representa el Hanan Pacha?",
            "opciones": ["a) Mundo inferior", "b) Mundo superior celestial", "c) Mundo presente", "d) Mundo animal"],
            "respuesta": "b"
        }
    ]
}

def jugar_mundo(nombre, mundo, data):
    print(f"\n{Colores.MORADO}↟ Estás ingresando a {mundo.upper()} ↟{Colores.RESET}")
    time.sleep(1.5)

    if mundo == "Uku Pacha":
        print(Colores.ROJO + "~ ~ ~ ~ 🐍 Serpiente ancestral ~ ~ ~ ~" + Colores.RESET)
    elif mundo == "Kay Pacha":
        print(Colores.VERDE + "/\\_/\\  /ὠ.ꞈ.Ὗ\\  → Puma del presente" + Colores.RESET)
    elif mundo == "Hanan Pacha":
        print(Colores.CIAN + "🦅 Cóndor sagrado - Visión espiritual y guía" + Colores.RESET)

    # Primera pregunta
    pregunta = random.choice(data)
    print("\n" + Colores.AMARILLO + pregunta["pregunta"] + Colores.RESET)
    for opcion in pregunta["opciones"]:
        print(opcion)
    r = input("Tu respuesta: ").lower()
    if r == pregunta["respuesta"]:
        print(Colores.VERDE + "✔️ Bien hecho. Has armonizado este plano del ser." + Colores.RESET)
        return 2
    else:
        print(Colores.ROJO + f"✖️ Respuesta incorrecta. La opción correcta era '{pregunta['respuesta']}'." + Colores.RESET)
        retry = input("¿Quieres intentar otra pregunta? (s/n): ").lower()
        if retry == 's':
            # Segunda pregunta (intenta evitar repetir)
            remaining = [p for p in data if p != pregunta]
            if remaining:
                pregunta = random.choice(remaining)
            else:
                pregunta = random.choice(data)  # Si no hay más, permite repetir
            print("\n" + Colores.AMARILLO + pregunta["pregunta"] + Colores.RESET)
            for opcion in pregunta["opciones"]:
                print(opcion)
            r = input("Tu respuesta: ").lower()
            if r == pregunta["respuesta"]:
                print(Colores.VERDE + "✔️ Bien hecho en el segundo intento." + Colores.RESET)
                return 1
            else:
                print(Colores.ROJO + f"✖️ Respuesta incorrecta. La opción correcta era '{pregunta['respuesta']}'." + Colores.RESET)
                return 0
        else:
            return 0

def final(nombre, puntaje):
    print(Colores.MORADO + "\n╔══════════════════════════════╗")
    print(f"   Final del viaje, {nombre}")
    print("╚══════════════════════════════╝" + Colores.RESET)
    print(f"Tu armonía alcanzada: {puntaje}/6")

    if puntaje == 6:
        print(Colores.VERDE + "Has alcanzado la armonía perfecta en los tres planos. Eres un maestro de la chakana, con energía fluyendo en equilibrio total." + Colores.RESET)
    elif puntaje >= 4:
        print(Colores.CIAN + "Buen equilibrio alcanzado. Continúa tu camino de integración interior; estás cerca de la maestría." + Colores.RESET)
    else:
        print(Colores.ROJO + "🌒 El sendero se revela paso a paso. Profundiza en la introspección y transforma; el equilibrio te espera." + Colores.RESET)

def main():
    nombre = bienvenida()
    total = 0
    mundos = ["Uku Pacha", "Kay Pacha", "Hanan Pacha"]
    random.shuffle(mundos)

    for m in mundos:
        total += jugar_mundo(nombre, m, preguntas[m])
        time.sleep(1.2)

    final(nombre, total)

if __name__ == "__main__":
    main()