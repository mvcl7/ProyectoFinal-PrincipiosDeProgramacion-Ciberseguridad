import shutil
import sys

def verificar_dependencias():
    if not shutil.which("nmap"):
        print("=" * 50)
        print("  ERROR: nmap no está instalado.")
        print("  Ejecutá primero: python setup.py")
        print("=" * 50)
        sys.exit(1)
    try:
        import nmap
    except ImportError:
        print("=" * 50)
        print("  ERROR: python-nmap no está instalado.")
        print("  Ejecutá primero: python setup.py")
        print("=" * 50)
        sys.exit(1)

def menu():
    print("=" * 50)
    print("Bienvenido al sistema de gestión de Puertos")
    print("1. Ver/seleccionar dispositivo a analizar")
    print("2. Editar puertos")
    print("3. Detectar vulnerabilidades")
    print("4. Salir")
    print("=" * 50)

verificar_dependencias()
menu()