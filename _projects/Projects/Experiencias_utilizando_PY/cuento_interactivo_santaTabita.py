import time
import sys
import random

# Colores ANSI para animación y contexto visual
COLORES = {
    "reset": "\033[0m",
    "titulo": "\033[1;34m",  # Azul bold
    "descripcion": "\033[0;32m",  # Verde
    "dialogo": "\033[1;33m",  # Amarillo bold
    "pregunta": "\033[1;35m",  # Magenta
    "arte": "\033[1;36m",  # Cian para ASCII art
    "opcion": "\033[1;31m"   # Rojo para opciones interactivas
}

# Función para efecto de spinner (animación de carga)
def spinner(mensaje, duracion=3):
    sys.stdout.write(f"{COLORES['descripcion']}{mensaje} {COLORES['reset']}")
    chars = ['|', '/', '-', '\\']
    for _ in range(duracion * 4):
        for char in chars:
            sys.stdout.write(f"\b{char}")
            sys.stdout.flush()
            time.sleep(0.1)
    print("\n")

# Función para imprimir con efecto animado y color variable
def imprimir_con_efecto(texto, color=COLORES["reset"], delay=0.02):
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0, 0.01))  # Delay variable para más dinamismo
    sys.stdout.write(COLORES["reset"] + "\n")

# Arte ASCII simple para ilustraciones en el cuento
artes_ascii = {
    "castillo": """
       /\\
      //\\\\ 
     //__\\\\
    //____\\\\
   //______\\\\
  Castillo Mágico
    """,
    "sueno": """
    ZzZ
   ( -.- )
    ZzZ
Sueño Profundo
    """,
    "mujer": """
     O
    /|\\
    / \\
Santa Tabita
    """,
    "cuadro": """
   _____
  |     |
  | ART |
  |_____|
Cuadro Mágico
    """
}

# Cuento adaptado: Integrado con elementos culturales ecuatorianos (mitos andinos, arte de Cuenca, tradiciones espirituales como el respeto a ancestros y ayuda comunitaria), para niños de subnivel Elemental (6-8 años). Promueve expresión emocional a través de sueños y arte, valoración del patrimonio plurinacional, creatividad onírica, y uso de narrativas interactivas para fomentar empatía y reflexión. Incluye más interacción: elecciones del usuario que alteran partes del cuento, preguntas socioemocionales, y actividades artísticas sugeridas.
cuento = {
    "titulo": "El Sueño Mágico de Santa Tabita (Integración de Artes, Sueños y Patrimonio Ecuatoriano)",
    "partes": [
        {
            "texto": """Hace siglos, en las tierras encantadas de Ecuador, donde los mitos andinos se entretejen con el arte de Cuenca, vivía un joven llamado Marco. Marco amaba dibujar paisajes serranos con colores inspirados en tejidos otavaleños y escuchar música tradicional como pasillos, expresando sus emociones creativamente.

En sus sueños, recreaba héroes de leyendas quichuas destinados a salvar a mujeres en apuros, valorando el patrimonio cultural plurinacional.""",
            "pregunta": "¿Qué harías tú en un sueño mágico? Elige: 1) Dibujar un héroe andino, 2) Cantar una canción amazónica.",
            "opciones": {
                "1": "¡Buena elección! Marco decide dibujar un héroe con patrones indígenas, fomentando la creatividad visual.",
                "2": "¡Excelente! Marco canta una melodía shuar, integrando música y emociones."
            },
            "arte": artes_ascii["sueno"]
        },
        {
            "texto": """Una noche, al escuchar una canción envolvente de marimbas costeñas, Marco se durmió profundamente. Apareció en un castillo envuelto en sombras, similar a las iglesias coloniales de Cuenca, con resonancias ancestrales. Allí encontró guardianes extraños, como espíritus de volcanes andinos.

Para subir al pasillo superior, debía evitarlos con astucia creativa.""",
            "pregunta": "¿Cómo ayudarías a Marco a evitar los guardianes? Elige: 1) Bailando una danza cañari, 2) Actuando una escena dramática tsáchila.",
            "opciones": {
                "1": "¡Genial! Marco baila con movimientos circulares, honrando tradiciones festivas como Inti Raymi.",
                "2": "¡Creativo! Marco actúa con gestos, promoviendo artes dramáticas y empatía cultural."
            },
            "arte": artes_ascii["castillo"]
        },
        {
            "texto": """Justo antes de llegar al último cuarto, se despertó. Pasaron años, pero nunca olvidó el castillo. Cuando enfrentó un problema socioemocional, como sentir soledad, volvió a soñar. Esta vez, la puerta estaba abierta. Dentro encontró a una mujer serena rezando: Santa Tabita, inspirada en figuras espirituales de ayuda comunitaria, como en las tradiciones ecuatorianas de solidaridad.

Marco no la reconoció al principio, pero sintió una conexión profunda, como en las leyendas de sanación ancestral.""",
            "pregunta": "¿Qué emoción sientes al encontrar a alguien misterioso? Elige: 1) Curiosidad, 2) Alegría, y explica por qué.",
            "opciones": None,  # Respuesta abierta
            "arte": artes_ascii["mujer"]
        },
        {
            "texto": """Se despertó murmurando: 'Tal vez sea una simple imaginación… las lecturas de mitos ecuatorianos trastocaron mi infancia.' Transcurrieron diez años. Ahora, en su habitación de Cuenca, soñó sentado contemplando una imagen de una mujer como princesa, con tonos azulados y morados, enmarcada en dorado, similar a los cuadros de museos cuencanos.

Intentó convencerse: 'Solo es una fantasía onírica.' Se enfadó, sintiendo culpa por creer en mundos inexplicables, pero enseña a expresar emociones a través del arte para sanar.""",
            "pregunta": "¿Crearías un dibujo de tu sueño? Elige: 1) Sí, con colores andinos, 2) No, prefiero contarlo en una canción.",
            "opciones": {
                "1": "¡Arte visual! Dibuja en casa inspirado en patrimonios de Cuenca.",
                "2": "¡Música! Inventa una letra sobre sueños para compartir en clase."
            },
            "arte": artes_ascii["cuadro"]
        },
        {
            "texto": """Pasaron dos años. Preparándose para viajar, alguien se le apareció: era similar a Santa Tabita del sueño. Resultó ser una voluntaria en un grupo altruista, ayudando con mirada luminosa, reflejando valores ecuatorianos de comunidad y diversidad.

No preguntó su nombre, pero supo que era del alma. Partió, pero desde entonces, cada 25 de octubre, en Ecuador, si llueve, los niños piden milagros a mediodía o saludan a Santa Tabita a las 5:00 p.m. para sanación y amor verdadero, integrando espiritualidad y arte en tradiciones.""",
            "pregunta": "¿Qué milagro pedirías a Santa Tabita? ¡Escribe tu deseo y dibújalo!",
            "opciones": None,  # Respuesta abierta
            "arte": artes_ascii["mujer"]
        }
    ]
}

def narrar_cuento():
    imprimir_con_efecto("\nBienvenido al Cuento Interactivo Mágico de Santa Tabita: ¡Explora sueños, arte y cultura ecuatoriana!", COLORES["titulo"], 0.03)
    spinner("Cargando el sueño mágico...")
    imprimir_con_efecto(f"\n{cuento['titulo']}", COLORES["titulo"], 0.05)
    
    for parte in cuento["partes"]:
        imprimir_con_efecto(parte["arte"], COLORES["arte"], 0.05)  # Ilustración ASCII
        # Imprimir texto con colores diferenciados
        for linea in parte["texto"].split('\n'):
            if linea.startswith('"') or linea.endswith('"'):  # Detectar diálogos
                imprimir_con_efecto(linea, COLORES["dialogo"])
            else:
                imprimir_con_efecto(linea, COLORES["descripcion"])
        
        # Interacción
        imprimir_con_efecto(parte["pregunta"], COLORES["pregunta"])
        if parte["opciones"]:
            respuesta = input("Tu elección (1/2): ")
            if respuesta in parte["opciones"]:
                imprimir_con_efecto(parte["opciones"][respuesta], COLORES["opcion"])
            else:
                imprimir_con_efecto("¡Elige 1 o 2 para continuar la aventura!", COLORES["opcion"])
        else:
            input("Tu respuesta: ")  # Respuesta abierta
            imprimir_con_efecto("¡Buena reflexión! Sigamos con el cuento.", COLORES["opcion"])
    
    imprimir_con_efecto("\nFin del cuento. ¡Reflexiona sobre tus sueños y crea arte inspirado en el patrimonio ecuatoriano!", COLORES["reset"])
    imprimir_con_efecto("Actividad: Dibuja tu versión del castillo o compone una canción sobre Santa Tabita.", COLORES["pregunta"])

# Ejecutar el cuento interactivo
narrar_cuento()