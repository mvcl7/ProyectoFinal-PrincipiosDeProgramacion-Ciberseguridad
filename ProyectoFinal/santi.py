import nmap
nm = nmap.PortScanner()

host = input("Ingresá la IP a escanear: ")
puerto = input("Ingresá el puerto a escanear: ")

nm.scan(host, puerto)

for host in nm.all_hosts():
    print(f"Nmap scan report for {host}")
    print(f"Host is {nm[host].state()}")
    print()
    print(f"{'PORT':<10} {'STATE':<10} {'SERVICE'}")
    print("-" * 30)
    
    for proto in nm[host].all_protocols():
        for puerto in nm[host][proto].keys():
            estado = nm[host][proto][puerto]['state']
            nombre = nm[host][proto][puerto]['name']
            print(f"{str(puerto)+'/'+proto:<10} {estado:<10} {nombre}")