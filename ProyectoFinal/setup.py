import subprocess
import sys
import platform
import shutil

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
        print("""
  En Windows nmap debe instalarse manualmente:
  1. Entrá a: https://nmap.org/download.html
  2. Descargá el instalador 'Latest stable release self-installer'
  3. Ejecutalo y seguí los pasos
  4. Reiniciá la terminal y volvé a correr este setup.py
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