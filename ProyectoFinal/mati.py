import sys
import os
import subprocess
import ctypes

def es_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def relanzar_como_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit(0)

def editar_puertos():
    puerto = input("¿Que puerto desea filtrar? ").strip()

    if not puerto.isdigit() or not (1 <= int(puerto) <= 65535):
        print("Error: El puerto debe ser un número entre 1 y 65535.")
        return

    sistema = sys.platform

    if sistema == "linux":
        print(f"Aplicando filtrado en Linux (UFW) para el puerto {puerto}: ")
        try:
            subprocess.run(['sudo', 'ufw', 'prepend', 'deny', f'{puerto}/tcp'], check=True)
            subprocess.run(['sudo', 'ufw', 'reload'], capture_output=True, check=True)
            print(f"Éxito, el puerto {puerto} ahora está filtrado.")
        except Exception as e:
            print(f"Error: Asegúrate de tener instalado UFW y ejecutar con permisos.")

    elif sistema == "win32":
        if not es_admin():
            print("\n  Se necesitan permisos de administrador.")
            respuesta = input("  ¿Querés relanzar el programa como administrador? (s/n): ").strip().lower()
            if respuesta == "s":
                relanzar_como_admin()
            else:
                print("  Operación cancelada.")
            return
        print(f"Aplicando filtrado en Windows para el puerto {puerto}: ")
        try:
            comando_windows = [
                'netsh', 'advfirewall', 'firewall', 'add', 'rule',
                f'name=Filtro_Permanente_{puerto}',
                'dir=in', 'action=block', 'protocol=TCP', f'localport={puerto}'
            ]
            subprocess.run(comando_windows, check=True)
            print(f"Exito, el puerto {puerto} ahora esta filtrado.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Sistema operativo no compatible.")