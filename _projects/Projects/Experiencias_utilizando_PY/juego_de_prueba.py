import random

# Frases de Dostoievski y fábulas de Esopo
dostoievski_frases = [
    "La enfermedad del alma es más peligrosa que la enfermedad del cuerpo.",
    "El hombre es un misterio. Hay que entenderlo, y si lo entiendes, perdonarlo.",
    "El dolor es el más grande maestro del hombre.",
    "En la vida de un hombre siempre hay un momento en que el hombre se decide entre la razón y el sentimiento."
]

esopo_fabulas = [
    "La zorra y las uvas: Es mejor renunciar que arriesgarse a lo imposible.",
    "La liebre y la tortuga: La paciencia y la constancia vencen al talento.",
    "El cuervo y la zorra: No dejes que la vanidad te nuble el juicio.",
    "La gallina de los huevos de oro: La codicia puede destruir lo que tenemos."
]

# Frases del Tao Te Ching
tao_te_ching_frases = [
    "El que conoce a los demás es sabio. El que se conoce a sí mismo es iluminado.",
    "Quien se adapta a la corriente fluida de la vida, encuentra la paz.",
    "Un árbol que crece al viento, resiste mejor la tormenta.",
    "Cuando te dejas llevar por el Tao, todo se acomoda por sí mismo."
]

# Función para obtener una frase según el estado emocional
def obtener_frase(estado):
    if estado.lower() == "bien":
        return random.choice(dostoievski_frases) + " " + random.choice(esopo_fabulas)
    else:
        return random.choice(tao_te_ching_frases)

# Función principal del juego
def juego():
    print("Bienvenido al juego de frases interactivas.")
    while True:
        # Pregunta sobre el estado emocional
        estado = input("¿Cómo estás? (bien/mal): ").strip()

        # Obtener y mostrar la frase correspondiente
        frase = obtener_frase(estado)
        print(f"\nFrase o fábula: {frase}\n")

        # Preguntar si desea continuar
        continuar = input("¿Deseas continuar con el juego? (sí/no): ").strip().lower()
        if continuar != "sí":
            print("Gracias por jugar. ¡Hasta pronto!")
            break

# Llamada a la función para iniciar el juego
if __name__ == "__main__":
    juego()

