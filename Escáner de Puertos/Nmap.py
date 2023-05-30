#Jesus Israel Bolaños Uvalle
#2005587

import nmap
escaner = nmap.PortScanner()
opcion = int(input("""Menú
                    1.- Escaneo UDP
                    2.-Escaneo completo
                    3.- Detectar sistema operativo
                    4.- Escaneo de red con  ping
                    """))
if opcion == 1:
    ip = input("Ingrese la direccion ip a escanear")
    puerto1 = input("ingrese el puerto con el que desea comenzar el escaneo")
    puerto2 = input("ingrese el puerto con el que desea terminar el escaneo")
    print("iniciando escaneo udp...")
    escaner.scan(ip, puerto1 + '-' + puerto2, '-sU')
    for host in escaner.all_hosts():       # Devolver la lista de host escaneada a host
        print('Host : %s (%s)' % (host,escaner[host].hostname()))   
        print('State : %s' % escaner[host].state())                 
        for proto in escaner[host].all_protocols():                 
            print('protocol : %s' % proto )                     # Salida del protocolo ejecutado
            lport = escaner[host][proto].keys()                      # Obtenga el puerto abierto por el host de destino y asígnelo a lport
        # lport.sort()
            for port in lport:                                                                  # Asignar lport a puerto y atravesar
                print('port : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))
if opcion ==2:
    ip = input("Ingrese la direccion ip a escanear")
    print("iniciando escaneo completo")
    escaner.scan(ip)
    for host in escaner.all_hosts():       # Devolver la lista de host escaneada a host
        print('Host : %s (%s)' % (host,escaner[host].hostname()))    
        print('State : %s' % escaner[host].state())                  
        for proto in escaner[host].all_protocols():                  
            print('protocol : %s' % proto )                     # Salida del protocolo ejecutado
            lport = escaner[host][proto].keys()                      # Obtenga el puerto abierto por el host de destino y asígnelo a lport

            for port in lport:                                                                  # Asignar lport a puerto y atravesar
                print('port : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))
if opcion==3:
    ip = input("Ingrese la direccion ip a escanear")
    scan_raw_result = escaner.scan(ip, arguments='-v -n -A')
    # Analizar resultados de escaneo
    for host, result in scan_raw_result['scan'].items():
        if result['status']['state'] == 'up':
            for os in result['osmatch']:
                print('El sistema operativo es:' + os['name'] + ' ' * 3)
if opcion ==4:
    ip=input("Ingrese la ip que desea escanear")
    #
    escaner.scan(hosts=ip, arguments='-sP')
    print("iniciando escaneo con ping...")
    for host in escaner.all_hosts():       # Devolver la lista de host escaneada a host

        print('Host : %s (%s)' % (host,escaner[host].hostname()))   
        print('State : %s' % escaner[host].state())                 
        for proto in escaner[host].all_protocols():                 

            print('protocol : %s' % proto )                     # Salida del protocolo ejecutado
            lport = escaner[host][proto].keys()                      # Obtenga el puerto abierto por el host de destino y asígnelo a lport
        # lport.sort()
            for port in lport:                                                                  # Asignar lport a puerto y atravesar
                print('port : %s\tstate : %s' % (port,escaner[host][proto][port]['state']))
    
