import os
from datetime import datetime

CARPETA_DIARIO = "diario_entradas"

def crear_carpeta_si_no_existe():
    if not os.path.exists(CARPETA_DIARIO):
        os.makedirs(CARPETA_DIARIO)

def obtener_nombre_archivo():
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(CARPETA_DIARIO, f"{fecha_actual}.md")

def agregar_entrada():
    print("\n📔 Bienvenido a tu Diario Electrónico")
    print("Escribe tu entrada. Para terminar, escribe una línea con solo 'FIN'.\n")

    lineas = []
    while True:
        linea = input()
        if linea.strip().upper() == "FIN":
            break
        lineas.append(linea)

    contenido = "\n".join(lineas)
    archivo = obtener_nombre_archivo()

    with open(archivo, "a", encoding="utf-8") as f:
        f.write(f"\n## Entrada: {datetime.now().strftime('%H:%M:%S')}\n")
        f.write(contenido + "\n\n---\n")

    print(f"\n✅ Entrada guardada en: {archivo}")

def main():
    crear_carpeta_si_no_existe()
    agregar_entrada()

if __name__ == "__main__":
    main()
