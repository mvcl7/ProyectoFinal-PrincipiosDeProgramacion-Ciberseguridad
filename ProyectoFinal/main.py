import sys
import shutil
import santi
import gaston

def verificar_dependencias():
    if not shutil.which("nmap"):
        print("=" * 50)
        print("  ERROR: nmap no está instalado.")
        print("  Ejecutá primero: python setup.py")
        print("=" * 50)
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

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case '1':
                santi.ver_dispositivo()
            case '2':
                print("\n  Esta opción está en desarrollo.")
            case '3':
                gaston.detectar_vulnerabilidades()
            case '4':
                sys.exit(0)
            case _:
                print("\n  Opción inválida.")

verificar_dependencias()
menu()