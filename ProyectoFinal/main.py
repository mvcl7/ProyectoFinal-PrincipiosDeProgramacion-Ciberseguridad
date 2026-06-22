import sys
import shutil
import os
import webbrowser
import santi
import gaston

NMAP_URL = "https://nmap.org/download.html"
NMAP_PATH_WINDOWS = r"C:\Program Files (x86)\Nmap"

def verificar_nmap():
    # Agrega la ruta de nmap al PATH por si no está registrada
    if os.name == "nt":
        os.environ["PATH"] += f";{NMAP_PATH_WINDOWS}"

    if shutil.which("nmap"):
        return True

    # nmap no está instalado
    print()
    print("=" * 55)
    print("  ERROR: nmap no está instalado en este sistema.")
    print()
    print("  Para usar el programa necesitás instalar nmap.")
    print(f"  Descargalo desde: {NMAP_URL}")
    print()
    print("  Pasos:")
    print("  1. Se va a abrir el navegador con la página de descarga.")
    print("  2. Descargá 'Latest stable release self-installer'")
    print("  3. Ejecutalo como administrador y seguí los pasos.")
    print("  4. Reiniciá el programa.")
    print("=" * 55)
    print()

    abrir = input("  ¿Querés abrir la página de descarga ahora? (s/n): ").strip().lower()
    if abrir == "s":
        webbrowser.open(NMAP_URL)
        print()
        print("  Navegador abierto. Una vez instalado nmap, volvé a ejecutar el programa.")

    input("\n  Presioná Enter para salir...")
    sys.exit(1)

def menu():
    while True:
        print()
        print("=" * 50)
        print("  Bienvenido al sistema de gestión de Puertos")
        print("=" * 50)
        print("  1. Ver/seleccionar dispositivo a analizar")
        print("  2. Editar puertos (en desarrollo)")
        print("  3. Detectar vulnerabilidades")
        print("  4. Salir")
        print("=" * 50)

        opcion = input("  Seleccione una opción: ").strip()

        match opcion:
            case '1':
                santi.ver_dispositivo()
            case '2':
                print("\n  Esta opción está en desarrollo.")
            case '3':
                gaston.detectar_vulnerabilidades()
            case '4':
                print("\n  Saliendo del programa.")
                sys.exit(0)
            case _:
                print("\n  Opción inválida. Ingrese 1, 2, 3 o 4.")

verificar_nmap()
menu()