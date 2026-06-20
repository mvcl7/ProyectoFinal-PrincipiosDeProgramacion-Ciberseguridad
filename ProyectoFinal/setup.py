import subprocess
import sys
import platform
import shutil
import os

def verificar_pip():
    print("Verificando pip...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "--version"],
                       check=True, capture_output=True)
        print("  pip está disponible.")
        return True
    except subprocess.CalledProcessError:
        print("  pip no encontrado. Intentando instalarlo...")
        subprocess.run([sys.executable, "-m", "ensurepip", "--upgrade"])
        return True

def instalar_python_nmap():
    print("Instalando python-nmap...")
    subprocess.run([sys.executable, "-m", "pip", "install", "python-nmap"],
                   check=True)
    print("  python-nmap instalado correctamente.")

def instalar_nmap_sistema():
    sistema = platform.system()
    print(f"Sistema operativo detectado: {sistema}")

    if shutil.which("nmap"):
        print("  nmap ya está instalado en el sistema.")
        return

    if sistema == "Windows":
        instalador = os.path.join(os.path.dirname(__file__), "instaladores", "nmap-setup.exe")
        if os.path.exists(instalador):
            print("  Instalando nmap desde el instalador incluido...")
            subprocess.run(['powershell', 'Start-Process', instalador, '-Verb', 'RunAs', '-Wait'], check=True)
            print("  nmap instalado. Reiniciá la terminal y volvé a correr setup.py para verificar.")
        else:
            print("""
            Instalador no encontrado en la carpeta 'instaladores/'.
            Descargalo manualmente desde: https://nmap.org/download.html
            """)

    elif sistema == "Linux":
        print("  Instalando nmap con apt...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "nmap"], check=True)
        print("  nmap instalado correctamente.")

    elif sistema == "Darwin":  # Mac
        if not shutil.which("brew"):
            print("  Homebrew no encontrado. Instalando Homebrew primero...")
            subprocess.run(
                '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',
                shell=True, check=True
            )
        print("  Instalando nmap con brew...")
        subprocess.run(["brew", "install", "nmap"], check=True)
        print("  nmap instalado correctamente.")

    else:
        print(f"  Sistema '{sistema}' no reconocido. Instalá nmap manualmente desde https://nmap.org")

def main():
    print("=" * 50)
    print("  Setup - Sistema de Gestión de Puertos")
    print("=" * 50)

    verificar_pip()
    instalar_python_nmap()
    instalar_nmap_sistema()

    print()
    print("=" * 50)
    print("  Setup completado. Ya podés usar el proyecto.")
    print("=" * 50)

main()