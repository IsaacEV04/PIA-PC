#!/bin/bash
#
# Escaner de puertos usando archivo especial en /dev
#
# Definicion de variables
direccion_ip=$1
puertos="20,21,22,23,24,25,50,51,53,54,74,54,34,66,43,111,221,211,121,144,243,356,23,167,646,773"
#Verificando que parametro ip no vengan vacio
[ $# -eq 0 ] && { echo "Modo de uso: $0 <direccion ip>"; exit 1; }
#
# Bucle for para cada puerto $puertos
#
IFS=,
for port in $puertos
do
    timeout 1 bash -c "echo > /dev/tcp/$direccion_ip/$port > /dev/null 2>&1" &&\
    echo $direccion_ip":"$port" is open"\
    ||\
    echo $direccion_ip":"$port" is closed"
done