#!/usr/bin/python
# Jesús Israel Bolaños Uvalle
# 2005587
# -*- coding: utf-8 -*-
#Partel
#Importamos librerias necesarias
import sys
from socket import *
#Parte2
#Modo de ejecución del script
host = sys.argv[1]
portstrs = sys.argv[2].split('-')
#Parte3
start_port = int(portstrs[0])
end_port = int(portstrs[1])
#Parte4
target_ip = gethostbyname(host)
opened_ports = []
#parte5
for port in range(start_port, end_port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        opened_ports.append(port)
#parte6
print("Opened ports:")
#
for i in opened_ports:
    print(i)
