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
    "arte": "\033[1;36m"  # Cian para ASCII art
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

# Arte ASCII simple para ilustraciones en cada cuento
artes_ascii = [
    """
     /\\
    //\\\\ 
   //__\\\\
  //____\\\\
 //______\\\\
Cóndor en vuelo
    """,
    """
    ~~~
   ~ ~ ~
  ~  ~  ~
 Río Amazonas
    """,
    """
    \\O/
     |
    / \\
Danza del Sol
    """,
    """
    O
   /|\\
   / \\
Marioneta
    """,
    """
    ___
   /   \\
  | ECU |
   \\___/
Mapa Mágico
    """
]

# Lista de cuentos enriquecidos con más contexto ECA
cuentos = [
    {
        "titulo": "El Cóndor Pintor (Artes Visuales y Patrimonio Andino - OI.2.7, OI.2.10, OI.2.11)",
        "texto": """En las majestuosas montañas andinas de Ecuador, donde el volcán Chimborazo toca el cielo como en las leyendas quichuas ancestrales, vivía una niña llamada Inti. Según el currículo ECA, Inti aprendía a expresar sus emociones a través de dibujos y colores naturales, valorando el patrimonio cultural como los tejidos otavaleños llenos de símbolos indígenas (ECA.2.3.9).

Un día soleado, un cóndor mágico, guardián de la diversidad plurinacional, se acercó y dijo: "¡Inti, ayúdame a pintar el cielo con creatividad para proteger nuestra herencia!" Inti, inspirada en las tradiciones de sus abuelos, usó achiote rojo y hojas verdes para crear patrones que representaban el sol Inti y la luna Quilla, fomentando la experimentación artística (OI.2.11).

Pero un viento fuerte, como las tormentas andinas, borró todo. Inti recordó las lecciones ECA sobre respeto a la naturaleza y diversidad: "La creatividad nace del corazón y une culturas". Dibujó murales colectivos con amigos, integrando artes visuales y documentando con fotos simples, como sugiere O.ECA.2.6 para usar tecnologías en la creación.

Al final, el cóndor voló feliz, y Inti enseñó a otros niños a valorar el patrimonio mediante proyectos artísticos. Esto promueve la expresión emocional y la apreciación cultural, clave en ECA.""",
        "pregunta": "¿Qué emoción expresarías tú pintando un volcán andino? ¡Dibuja y comparte!",
        "arte": artes_ascii[0]
    },
    {
        "titulo": "La Canción del Río Amazonas (Música y Folclore Amazónico - OI.2.7, OI.3.10, ECA.3.2.13)",
        "texto": """En la exuberante selva amazónica ecuatoriana, junto al río Napo donde habitan pueblos como los shuar y waoranis, un niño llamado Yaku creaba melodías con instrumentos de bambú, imitando sonidos de la naturaleza para expresar emociones, tal como indica OI.2.7 del ECA.

Una noche estrellada, el espíritu del río, un delfín rosado de mitos ancestrales, emergió cantando: "¡Yaku, compone una canción colectiva para salvar la selva y honrar nuestra diversidad cultural!" Yaku, recordando fiestas indígenas con marimbas tradicionales, improvisó ritmos que unían loros, monos y flores, valorando el patrimonio intangible (OI.3.10).

Una tormenta amenazó, pero Yaku usó su creatividad para grabar sonidos con herramientas simples, como en ECA.3.2.13, integrando música y tecnología. La canción calmó las aguas, enseñando empatía y sostenibilidad ambiental.

Hoy, Yaku comparte sus composiciones en escuelas, fomentando proyectos interdisciplinarios que combinan música con ciencia sobre la flora amazónica.""",
        "pregunta": "¿Qué sonido de la selva agregarías a una canción? ¡Inventa y canta!",
        "arte": artes_ascii[1]
    },
    {
        "titulo": "La Danza del Sol en Inti Raymi (Danza y Tradiciones Festivas - OI.2.11, OI.3.10, ECA.2.2.3)",
        "texto": """En las fértiles tierras serranas de Ecuador, durante el festival Inti Raymi que celebra la cosecha quichua y cañari, una niña llamada Raymi practicaba danzas circulares para expresar gratitud emocional, alineado con OI.2.11 del ECA sobre experimentación corporal.

El espíritu del maíz, de leyendas ancestrales, le susurró: "¡Baila con amigos para unir culturas y valorar el patrimonio!" Raymi integró pasos otavaleños y saraguros, creando coreografías colectivas que representaban el ciclo solar, promoviendo diversidad plurinacional (OI.3.10).

Cuando nubes ocultaron el sol, Raymi improvisó una danza grupal con elementos dramáticos, como en ECA.2.2.3, usando movimientos para contar historias de la tierra. El sol volvió, simbolizando unidad.

Raymi ahora enseña danzas en comunidades, integrando ECA con educación física para fomentar empatía y creatividad.""",
        "pregunta": "¿Cómo danzarías para celebrar una fiesta ecuatoriana? ¡Prueba y describe!",
        "arte": artes_ascii[2]
    },
    {
        "titulo": "El Teatro de las Marionetas Costeñas (Artes Dramáticas y Leyendas Costeras - OI.2.7, OI.4.10, ECA.2.3.11)",
        "texto": """En las soleadas playas costeras de Ecuador, con influencias montubias y afroecuatorianas, un niño llamado Mar construía marionetas de conchas para actuar leyendas tsáchilas, expresando emociones a través del drama (OI.2.7).

Una sirena mítica apareció: "¡Usa teatro para contar historias olvidadas y apreciar nuestra multiculturalidad!" Mar creó obras sobre pescadores y ballenas, con diálogos en ritmos tradicionales, valorando el patrimonio oral (OI.4.10).

Un olvido borró el guion, pero Mar improvisó gestos y voces, documentando con dibujos simples como tecnología básica (ECA.2.3.11). La sirena aplaudió la unión de identidades.

Mar presenta festivales teatrales, integrando drama con historia para promover respeto al océano y diversidad.""",
        "pregunta": "¿Qué personaje costero crearías en una marioneta? ¡Imagina y actúa!",
        "arte": artes_ascii[3]
    },
    {
        "titulo": "El Viaje Cultural Mágico (Integración de Artes y Patrimonio Nacional - OI.2.10, O.ECA.2.6, ECA.5.1.8)",
        "texto": """En el diverso Ecuador, una niña llamada Ecuadorita encontró un mapa mágico que conectaba sierra, amazonía, costa y Galápagos, para explorar patrimonio y expresar ideas creativamente (OI.2.10).

El mapa dijo: "¡Viaja con artes para valorar la plurinacionalidad!" Ecuadorita pintó tortugas galapagueñas (visuales), cantó pasillos serranos (música), danzó carnavales costeños (danza) y actuó mitos amazónicos (drama), usando herramientas digitales simples para documentar (O.ECA.2.6).

En un laberinto de olvido, creó una obra multimedia interdisciplinaria, como en ECA.5.1.8. El mapa reveló: "La creatividad conserva culturas".

Ecuadorita comparte viajes en escuelas, fomentando proyectos con tecnología para apreciación cultural.""",
        "pregunta": "¿Qué arte usarías para explorar una región ecuatoriana? ¡Crea tu idea!",
        "arte": artes_ascii[4]
    }
]

def menu():
    imprimir_con_efecto("\nBienvenido al Libro Mágico Animado de Cuentos ECA (Desarrollado por Marco): ¡Descubre la cultura ecuatoriana con creatividad y diversión!", COLORES["titulo"], 0.03)
    for i, cuento in enumerate(cuentos):
        imprimir_con_efecto(f"{i+1}. {cuento['titulo']}", COLORES["titulo"])
    choice = int(input("\nElige un número de cuento (1-5): ")) - 1
    if 0 <= choice < 5:
        spinner("Cargando el cuento mágico...")
        imprimir_con_efecto(cuentos[choice]['arte'], COLORES["arte"], 0.05)  # Ilustración ASCII
        imprimir_con_efecto(f"\n{cuentos[choice]['titulo']}", COLORES["titulo"], 0.05)
        # Imprimir texto con colores diferenciados
        for linea in cuentos[choice]['texto'].split('\n'):
            if linea.startswith('"') or linea.endswith('"'):  # Detectar diálogos aproximados
                imprimir_con_efecto(linea, COLORES["dialogo"])
            else:
                imprimir_con_efecto(linea, COLORES["descripcion"])
        imprimir_con_efecto("\nFin del cuento. ¡Reflexiona sobre el patrimonio cultural!", COLORES["reset"])
        imprimir_con_efecto(cuentos[choice]['pregunta'], COLORES["pregunta"])
        input("Tu respuesta: ")  # Interactividad
        print("\n¡Excelente! Sigue explorando con ECA.")
    else:
        print("Selección inválida. Intenta de nuevo.")
        menu()

# Ejecutar el menú
menu()