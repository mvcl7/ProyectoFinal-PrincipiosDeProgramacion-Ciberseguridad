import nmap
nm = nmap.PortScanner()

nm.scan('192.168.56.1', arguments='-A -sV --open -T4')

for host in nm.all_hosts():
    print(f"Nmap scan report for {host}")
    print(f"Host is {nm[host].state()}")
    print()
    print(f"{'PORT':<10} {'STATE':<10} {'SERVICE':<15} {'PRODUCT':<20} {'VERSION'}")
    print("-" * 70)
    
    for proto in nm[host].all_protocols():
        for puerto in nm[host][proto].keys():
            estado = nm[host][proto][puerto]['state']
            nombre = nm[host][proto][puerto]['name']
            producto = nm[host][proto][puerto]['product']
            version = nm[host][proto][puerto]['version']
            print(f"{str(puerto)+'/'+proto:<10} {estado:<10} {nombre:<15} {producto} {version}")