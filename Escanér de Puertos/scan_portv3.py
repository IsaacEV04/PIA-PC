#Nombre: Isaac Emilio Esparza Vazquez
#Matricula: 2012872

#!/usr/bin/python
# -*- coding: utf-8 -*-

#Parte1
#Importamos librerias necesarias
import sys
import threading
from socket import *

#Parte2
#Creamos una función tcp_test la cual 
#permite probar mediante socket los puertos
#abiertos, se le agrega lock.release()
def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        print("Opened port:", port)

#Parte3
#Establecemos el main del script
#Guardamos en variables host y portstrs
if __name__ == '__main__':
    # portscan.py <host> <start_port>-<end_port>
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')

    #Parte4
    #portstrs se convierte en lista al momento
    #de hacer split y de ahi obtener dos valores
    start_port = int(portstrs[0])
    end_port = int(portstrs[1])

    #Parte5
    #Usando la funcion gethostbyname se obtiene
    #la dirección ip.
    target_ip = gethostbyname(host)

    #Parte6
    #Se inicia bucle para probar puertos
    #Usando la función tcp_test y generando
    #un hilo por cada puerto a probar
    hilos = []
    for port in range(start_port, end_port):
        hilo = threading.Thread(target=tcp_test, args=(port,))
        hilos.append(hilo)
        hilo.start()