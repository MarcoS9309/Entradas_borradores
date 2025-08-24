import time
import sys

# Lista de cuentos alineados con ECA: cada uno integra una disciplina artística y elementos culturales ecuatorianos.
cuentos = [
    {
        "titulo": "El Cóndor Pintor (Artes Visuales y Patrimonio Andino)",
        "texto": """En las altas montañas de los Andes ecuatorianos, vivía una niña llamada Inti, que amaba dibujar con colores hechos de plantas ancestrales. Un día, un cóndor mágico, guardián de los volcanes como el Chimborazo, se posó en su ventana. "¡Ayúdame a pintar el cielo!", dijo el cóndor. Inti tomó sus pinceles y creó un arcoíris con tonos de la tierra andina: rojo como el achiote, verde como las esmeraldas de la sierra.

Juntos volaron sobre Quito, donde Inti vio tejidos otavaleños y mercados llenos de arte. Pero un viento fuerte borró sus dibujos. Inti recordó las tradiciones de sus abuelos: "La creatividad nace del corazón". Dibujó de nuevo, esta vez con patrones indígenas que representaban el sol y la luna. El cóndor, agradecido, le enseñó a respetar la naturaleza, como en las leyendas quichuas.

Desde entonces, Inti pinta murales en su pueblo, inspirando a otros niños a valorar el patrimonio cultural. ¿Y tú, qué dibujarías para proteger nuestras montañas?"""
    },
    {
        "titulo": "La Canción del Río Amazonas (Música y Folclore Amazónico)",
        "texto": """En la selva amazónica de Ecuador, un niño llamado Yaku vivía junto al gran río Napo. Yaku adoraba crear melodías con hojas y palos, imitando los sonidos de la naturaleza. Una noche, el espíritu del río, un delfín rosado de las leyendas shuar, apareció cantando: "¡Únete a mi canción para salvar la selva!".

Yaku tomó un instrumento hecho de bambú, similar a las marimbas tradicionales, y compuso una tonada con ritmos de los pueblos originarios. Cantaron sobre monos, loros y flores gigantes, pero una tormenta amenazó con inundar todo. Recordando las fiestas ancestrales, Yaku improvisó versos que unían a los animales en armonía.

La canción calmó la tormenta, y el delfín le dijo: "La música une a las culturas". Ahora, Yaku enseña a sus amigos a crear canciones que celebran la diversidad amazónica, como en las tradiciones de los waoranis. ¿Qué melodía inventarías para tu río?"""
    },
    {
        "titulo": "La Danza del Sol en Inti Raymi (Danza y Tradiciones Festivas)",
        "texto": """En las tierras fértiles de la sierra ecuatoriana, una niña llamada Raymi preparaba la fiesta del Inti Raymi, el festival del sol quichua. Raymi soñaba con danzar como sus ancestros, con pasos que imitaban el viento y las cosechas. Pero era tímida. Un espíritu del maíz, de las antiguas leyendas, le susurró: "¡Baila con el corazón para honrar nuestra herencia!".

Raymi practicó movimientos circulares, como las danzas indígenas con plumas y colores vibrantes. En la fiesta, unió a niños de diferentes pueblos: otavaleños, saraguros y cañaris. Cuando el sol se ocultaba, una nube tapó la luz, pero Raymi improvisó una danza colectiva que invocaba la unidad.

El sol brilló de nuevo, y todos celebraron la diversidad cultural. Raymi aprendió que la danza expresa emociones y conserva tradiciones. Hoy, enseña pasos del Inti Raymi en su escuela. ¿Cómo bailarías para festejar el sol?"""
    },
    {
        "titulo": "El Teatro de las Marionetas Costeñas (Artes Dramáticas y Leyendas Costeras)",
        "texto": """En las playas de la costa ecuatoriana, un niño llamado Mar vivía en un pueblo pesquero. Amaba crear marionetas con conchas y redes, inspirado en las leyendas montubias sobre el mar. Una tarde, una sirena de los mitos tsáchilas apareció: "¡Usa tu teatro para contar nuestras historias olvidadas!".

Mar construyó un escenario con madera de balsa y actuó una obra sobre pescadores y ballenas, con diálogos en ritmos afroecuatorianos. Pero un olvido borró las palabras. Recordando las tradiciones orales, Mar improvisó con gestos y voces, involucrando a sus amigos como actores.

La sirena aplaudió: "El teatro une identidades". Ahora, Mar presenta obras en festivales costeros, promoviendo el respeto al océano y la herencia multicultural. ¿Qué personaje crearías en tu marioneta?"""
    },
    {
        "titulo": "El Viaje Cultural Mágico (Integración de Artes y Patrimonio Nacional)",
        "texto": """En el corazón de Ecuador, una niña llamada Ecuadorita descubrió un mapa mágico que unía las regiones: sierra, amazonía, costa y Galápagos. El mapa, guardián de las tradiciones ancestrales, dijo: "¡Explora con arte para valorar nuestra diversidad!".

Ecuadorita pintó tortugas galapagueñas (artes visuales), cantó pasillos serranos (música), danzó en carnavales costeños (danza) y actuó leyendas amazónicas (teatro). Enfrentó un laberinto de olvido, pero creó una obra integrada con elementos plurinacionales.

El mapa reveló: "La creatividad conserva el patrimonio". Ecuadorita ahora comparte su viaje en escuelas, fomentando la identidad nacional. ¿Qué arte usarías para explorar Ecuador?"""
    }
]

def imprimir_con_efecto(texto, color="\033[0m", delay=0.03):
    """Función para imprimir texto con efecto de escritura animada y color."""
    sys.stdout.write(color)
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\033[0m\n")  # Reset color

def menu():
    """Menú interactivo para seleccionar cuento."""
    print("\nBienvenido al Libro Mágico de Cuentos ECA: ¡Explora la cultura ecuatoriana con creatividad!")
    for i, cuento in enumerate(cuentos):
        imprimir_con_efecto(f"{i+1}. {cuento['titulo']}", "\033[1;32m")  # Verde para títulos
    choice = int(input("\nElige un número de cuento (1-5): ")) - 1
    if 0 <= choice < 5:
        imprimir_con_efecto(f"\n{cuentos[choice]['titulo']}", "\033[1;34m", 0.05)  # Azul para título principal
        imprimir_con_efecto(cuentos[choice]['texto'], "\033[0m", 0.02)  # Texto normal con efecto
        print("\nFin del cuento. ¡Reflexiona y crea tu propia versión!")
    else:
        print("Selección inválida. Intenta de nuevo.")
        menu()

# Ejecutar el menú
menu()