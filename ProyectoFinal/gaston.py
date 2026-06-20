import nmap
import re
import os

os.environ["PATH"] += r";C:\Program Files (x86)\Nmap"

nm = nmap.PortScanner()

VERSIONES_SEGURAS = {
    "apache": {"version": "2.4.59", "url": "https://httpd.apache.org/download.cgi"},
    "nginx": {"version": "1.26.1", "url": "https://nginx.org/en/download.html"},
    "iis": {"version": "10.0", "url": "https://www.iis.net/downloads"},
    "lighttpd": {"version": "1.4.76", "url": "https://www.lighttpd.net/download/"},
    "caddy": {"version": "2.8.4", "url": "https://caddyserver.com/docs/install"},
    "openssh": {"version": "9.8", "url": "https://www.openssh.com/portable.html"},
    "dropbear": {
        "version": "2022.83",
        "url": "https://matt.ucc.asn.au/dropbear/releases/",
    },
    "vnc": {
        "version": "6.11.0",
        "url": "https://www.realvnc.com/en/connect/download/vnc/",
    },
    "rdp": {
        "version": "10.0",
        "url": "https://support.microsoft.com/en-us/windows/remote-desktop",
    },
    "vsftpd": {"version": "3.0.5", "url": "https://security.appspot.com/vsftpd.html"},
    "proftpd": {"version": "1.3.8", "url": "http://www.proftpd.org/docs/"},
    "filezilla": {
        "version": "1.8.2",
        "url": "https://filezilla-project.org/download.php?type=server",
    },
    "postfix": {"version": "3.9.0", "url": "https://www.postfix.org/download.html"},
    "sendmail": {
        "version": "8.18.1",
        "url": "https://www.proofpoint.com/us/open-source-email-solution",
    },
    "dovecot": {"version": "2.3.21", "url": "https://www.dovecot.org/download/"},
    "exim": {"version": "4.98", "url": "https://www.exim.org/mirrors.html"},
    "mysql": {"version": "8.4.0", "url": "https://dev.mysql.com/downloads/mysql/"},
    "mariadb": {"version": "11.4.2", "url": "https://mariadb.org/download/"},
    "postgresql": {"version": "16.3", "url": "https://www.postgresql.org/download/"},
    "mongodb": {
        "version": "7.0.11",
        "url": "https://www.mongodb.com/try/download/community",
    },
    "redis": {"version": "7.2.5", "url": "https://redis.io/download/"},
    "elasticsearch": {
        "version": "8.14.1",
        "url": "https://www.elastic.co/downloads/elasticsearch",
    },
    "mssql": {
        "version": "16.0",
        "url": "https://www.microsoft.com/en-us/sql-server/sql-server-downloads",
    },
    "bind": {"version": "9.18.28", "url": "https://www.isc.org/bind/"},
    "unbound": {
        "version": "1.20.0",
        "url": "https://nlnetlabs.nl/projects/unbound/download/",
    },
    "squid": {"version": "6.10", "url": "http://www.squid-cache.org/Versions/"},
    "haproxy": {"version": "2.9.9", "url": "https://www.haproxy.org/#down"},
    "varnish": {"version": "7.5.0", "url": "https://varnish-cache.org/releases/"},
    "snmp": {"version": "5.9.4", "url": "http://www.net-snmp.org/download.html"},
    "zabbix": {"version": "6.4.16", "url": "https://www.zabbix.com/download"},
    "nagios": {"version": "4.5.3", "url": "https://www.nagios.org/downloads/"},
    "docker": {"version": "27.0.3", "url": "https://docs.docker.com/engine/install/"},
    "kubernetes": {"version": "1.30.2", "url": "https://kubernetes.io/releases/"},
    "samba": {"version": "4.20.2", "url": "https://www.samba.org/samba/download/"},
    "openvpn": {"version": "2.6.11", "url": "https://openvpn.net/community-downloads/"},
    "tomcat": {
        "version": "10.1.24",
        "url": "https://tomcat.apache.org/download-10.cgi",
    },
    "jenkins": {"version": "2.462", "url": "https://www.jenkins.io/download/"},
    "php": {"version": "8.3.8", "url": "https://www.php.net/downloads"},
    "node": {"version": "20.15.0", "url": "https://nodejs.org/en/download/"},
    "nfs": {"version": "2.6.4", "url": "https://sourceforge.net/projects/nfs/"},
}


def parsear_version(v):
    return tuple(int(n) for n in re.findall(r"\d+", v)[:4])


def identificar_servicio(producto, nombre):
    texto = (producto + " " + nombre).lower()
    for clave in VERSIONES_SEGURAS:
        if clave in texto:
            return clave
    return None


def analizar_versiones(host):
    ancho = 110
    print()
    print("=" * ancho)
    print("  COMPARACION DE VERSIONES")
    print("=" * ancho)
    print(
        f"{'PUERTO':<12} {'SERVICIO':<35} {'VERSION DETECTADA':<22} {'VERSION MINIMA':<16} ESTADO"
    )
    print("-" * ancho)

    seguros = desact = sin_datos = 0

    for proto in nm[host].all_protocols():
        for puerto in nm[host][proto].keys():
            datos = nm[host][proto][puerto]
            producto = datos.get("product", "")
            nombre = datos.get("name", "")
            version = datos.get("version", "")
            clave = identificar_servicio(producto, nombre)
            puerto_str = f"{puerto}/{proto}"

            if not clave:
                sin_datos += 1
                servicio = (producto or nombre or "desconocido")[:34]
                print(
                    f"{puerto_str:<12} {servicio:<35} {version or 'N/A':<22} {'N/A':<16} No registrado"
                )
                continue

            info = VERSIONES_SEGURAS[clave]
            ver_min = info["version"]
            url = info["url"]

            if not version:
                sin_datos += 1
                print(
                    f"{puerto_str:<12} {clave:<35} {'N/A':<22} {ver_min:<16} Version no detectada"
                )
                continue

            if parsear_version(version) >= parsear_version(ver_min):
                seguros += 1
                print(
                    f"{puerto_str:<12} {clave:<35} {version:<22} {ver_min:<16} SEGURO"
                )
            else:
                desact += 1
                print(
                    f"{puerto_str:<12} {clave:<35} {version:<22} {ver_min:<16} DESACTUALIZADO"
                )
                print(f"{'':12} {'Actualizacion en:':<35} {url}")

    print("=" * ancho)
    print(
        f"  Resumen: {seguros} seguros | {desact} desactualizados | {sin_datos} sin datos"
    )
    print("=" * ancho)


def detectar_vulnerabilidades():
    iphost = input("Ingrese la dirección IP a analizar: ")
    print(f"\nEscaneando {iphost}... Esto puede tardar varios minutos.")
    nm.scan(iphost, arguments="-A -sV --open -T4")

    for host in nm.all_hosts():
        print(f"\nNmap scan report for {host}")
        print(f"Host is {nm[host].state()}")
        print()
        print(f"{'PORT':<10} {'STATE':<10} {'SERVICE':<15} {'PRODUCT':<35} {'VERSION'}")
        print("=" * 100)

        for proto in nm[host].all_protocols():
            for puerto in nm[host][proto].keys():
                estado = nm[host][proto][puerto]["state"]
                nombre = nm[host][proto][puerto]["name"]
                producto = nm[host][proto][puerto]["product"]
                version = nm[host][proto][puerto]["version"]
                print(
                    f"{str(puerto)+'/'+proto:<10} {estado:<10} {nombre:<15} {producto:<35} {version}"
                )
                print("-" * 100)

        respuesta = (
            input("\n¿Desea ver el análisis de versiones? (s/n): ").strip().lower()
        )
        if respuesta == "s":
            analizar_versiones(host)
