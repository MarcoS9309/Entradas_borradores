import random

# Definimos algunas respuestas y reflexiones relacionadas con el Yo
respuestas_yo = {
    "autoconocimiento": [
        "El autoconocimiento es la llave para comprender nuestra naturaleza más profunda. ¿Qué parte de ti te gustaría conocer mejor hoy?",
        "Conocerse a uno mismo no es un destino, sino un viaje continuo. ¿Qué aspectos de tu vida crees que aún no has explorado completamente?",
        "El camino del autoconocimiento es largo y a menudo desafiante, pero cada paso hacia el interior de tu ser es un avance hacia la plenitud.",
        "Para conocerte de verdad, es necesario enfrentarte a tus sombras. ¿Estás listo para explorar las partes de ti que has evitado?"
    ],
    "reflexion": [
        "La reflexión constante nos permite aclarar pensamientos, emociones y decisiones. ¿Qué piensas que deberías reflexionar más en tu vida?",
        "La reflexión es como un espejo del alma. ¿Qué es lo que ves cuando te miras en él?",
        "¿Cuándo fue la última vez que realmente te detuviste a pensar en lo que estás buscando en la vida?",
        "La verdadera reflexión no solo se da con la mente, sino también con el corazón. ¿Cómo te sientes respecto a las decisiones que has tomado últimamente?"
    ],
    "equilibrio": [
        "El equilibrio es clave para vivir de manera armónica. ¿Qué área de tu vida sientes que necesita más equilibrio?",
        "Para alcanzar la armonía interna, es necesario balancear las demandas externas con nuestras necesidades internas. ¿Cómo equilibras tu vida diaria?",
        "A veces buscamos el equilibrio en lo externo, pero el verdadero equilibrio comienza en nuestro interior. ¿Qué emociones o pensamientos deseas equilibrar?",
        "El equilibrio no es la ausencia de conflicto, sino la capacidad de gestionar los altibajos con serenidad. ¿Qué te causa más conflicto interno en este momento?"
    ],
    "sabiduria": [
        "La sabiduría no solo se encuentra en los libros, sino en las experiencias que vivimos cada día. ¿Qué lecciones importantes has aprendido últimamente?",
        "¿Qué es lo más sabio que has hecho hasta ahora en tu vida?",
        "La sabiduría es la capacidad de ver más allá de lo evidente, de comprender las lecciones ocultas en nuestras experiencias. ¿Hay algo que hayas aprendido de forma profunda en el último tiempo?",
        "La sabiduría llega cuando nos permitimos aprender de nuestras caídas y no solo de nuestros éxitos. ¿Qué lecciones has aprendido de tus fracasos?"
    ],
    "psique": [
        "La psique humana es compleja y rica en capas. ¿Qué aspectos de tu psique aún no comprendes completamente?",
        "A veces, nuestro inconsciente tiene respuestas que nuestra mente consciente no puede entender. ¿Te has encontrado alguna vez con una parte de ti mismo que no podías reconocer?",
        "La psique busca integrar las diferentes partes de nuestro ser. ¿Qué parte de ti sientes que está desconectada de tu vida actual?",
        "Explorar tu psique es un viaje profundo, pero esencial. ¿Qué parte de ti desearías explorar más a fondo?"
    ],
    "autocuidado": [
        "El autocuidado es una práctica constante que va más allá de los cuidados físicos. ¿Cómo te estás cuidando emocional y mentalmente en este momento?",
        "El autocuidado es un acto de respeto hacia ti mismo. ¿Qué pequeños actos de autocuidado puedes incorporar hoy en tu vida?",
        "El autocuidado comienza con escuchar tus necesidades internas. ¿Qué necesita tu cuerpo y tu mente hoy?",
        "A veces nos olvidamos de cuidarnos a nosotros mismos mientras cuidamos de los demás. ¿Cómo puedes equilibrar el cuidado hacia ti mismo y hacia los demás?"
    ]
}

def respuesta_yo(pregunta):
    """Función para generar respuestas del 'Yo' a partir de preguntas del usuario."""
    pregunta = pregunta.lower()
    if "autoconocimiento" in pregunta:
        return random.choice(respuestas_yo["autoconocimiento"])
    elif "reflexion" in pregunta:
        return random.choice(respuestas_yo["reflexion"])
    elif "equilibrio" in pregunta:
        return random.choice(respuestas_yo["equilibrio"])
    elif "sabiduria" in pregunta:
        return random.choice(respuestas_yo["sabiduria"])
    elif "psique" in pregunta:
        return random.choice(respuestas_yo["psique"])
    elif "autocuidado" in pregunta:
        return random.choice(respuestas_yo["autocuidado"])
    else:
        return "Interesante reflexión. ¿Qué piensas tú sobre esta pregunta? A veces, las respuestas más profundas vienen de dentro de nosotros."

def conversar_con_mi_yo():
    print("Bienvenido a una conversación profunda contigo mismo. Puedes preguntarme sobre autoconocimiento, equilibrio, reflexión, sabiduría, psique y autocuidado.")
    print("Para salir, escribe 'salir'.")
    
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == "salir":
            print("Yo: Ha sido un placer conversar contigo. Que encuentres el equilibrio y la paz interna en tu vida.")
            break
        respuesta = respuesta_yo(pregunta)
        print(f"Yo: {respuesta}")
        
        # Continuar con una reflexión profunda
        continuar = input("¿Deseas continuar con esta conversación? (sí/no): ")
        if continuar.lower() != "sí":
            print("Yo: Que el autoconocimiento te guíe siempre. Nos vemos en el próximo encuentro.")
            break

# Inicia la conversación
conversar_con_mi_yo()
