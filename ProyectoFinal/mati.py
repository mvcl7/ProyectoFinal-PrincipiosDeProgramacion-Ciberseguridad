import sys
import os
import subprocess

puerto = input("¿Que puerto desea filtrar? ").strip() #elimina los espacios en blanco
if not puerto.isdigit() or not (1 <= int(puerto) <= 65535):
    print("Error: El puerto debe ser un número entre 1 y 65535.")
    sys.exit(1)
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
        print(f"Error: Asegúrate de ejecutar este script abriendo la terminal como administrador.")
else:
    print("Sistema operativo no compatible.")
