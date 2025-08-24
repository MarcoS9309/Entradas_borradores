import random

# Lista de chistes
chistes = [
    "¿Por qué el libro de matemáticas está triste? Porque tenía demasiados problemas.",
    "¿Qué le dijo el uno al diez? Para ser como yo, tenés que ser sincero.",
    "¿Sabes cuál es el animal más antiguo? La cebra, porque es en blanco y negro.",
    "¿Qué le dijo el semáforo al coche? No me mires, me estoy cambiando.",
    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter."
]

# Lista de consejos
consejos = [
    "Recuerda que el bienestar emocional es igual de importante que el físico. Tómate un tiempo para ti mismo y busca la paz en las pequeñas cosas.",
    "La vida puede ser difícil, pero los momentos de dificultad nos enseñan lecciones valiosas. Respira profundo y sigue adelante.",
    "No te preocupes por los fracasos, cada error te acerca más al éxito. Aprender de ellos es lo que te hace más fuerte.",
    "Recuerda que la felicidad no es un destino, es una forma de viajar. Disfruta cada paso que das en tu camino.",
    "La paz interior proviene de saber que las cosas pasan por una razón. Confía en el proceso y en ti mismo."
]

# Lista de cuentos
cuentos = [
    "Había una vez un joven que caminaba por un bosque oscuro, buscando la sabiduría. Se encontró con un anciano que le dio un consejo: 'El verdadero conocimiento no está en las palabras, sino en la experiencia.' El joven siguió su camino y entendió que cada paso lo acercaba más a su sabiduría.",
    "Un gran río atravesaba la ciudad. Todos los habitantes temían cruzarlo, pero un anciano les dijo: 'El miedo es el mayor obstáculo. No hay río que no se pueda cruzar si tienes el coraje de dar el primer paso.' Desde ese día, los habitantes cruzaron el río con valentía.",
    "En un lejano pueblo, una anciana le dio un consejo a su nieto: 'La vida es como un jardín. Si siembras amabilidad, cosecharás paz. Si siembras odio, cosecharás dolor. Tú eliges qué tipo de jardín quieres tener.'"
]

# Función para manejar respuestas
def respuesta_usuario():
    while True:
        print("\nHola, ¿cómo estás?")
        respuesta = input("Tu respuesta: ").strip().lower()

        if "bien" in respuesta or "excelente" in respuesta or "genial" in respuesta:
            # Si la respuesta es positiva
            print("\n¡Me alegra saber que estás bien!")
            print("Aquí tienes un chiste: ", random.choice(chistes))
        else:
            # Si la respuesta es negativa
            print("\nParece que no te encuentras bien. Recuerda que todo pasa, y aquí te dejo un consejo.")
            print("Consejo:", random.choice(consejos))

            # Opción para contar un cuento
            contar_cuento = input("¿Te gustaría escuchar un cuento? (sí/no): ").strip().lower()
            if contar_cuento == "sí":
                print("\nAquí tienes un cuento:\n", random.choice(cuentos))

        # Pregunta si quiere seguir jugando
        continuar = input("\n¿Quieres seguir jugando? (sí/no): ").strip().lower()
        if continuar != "sí":
            print("¡Gracias por jugar! Espero que te haya ayudado a pasar un buen rato.")
            break

# Ejecutar la función
respuesta_usuario()
