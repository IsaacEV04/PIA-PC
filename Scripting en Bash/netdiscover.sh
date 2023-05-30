#!/bin/bash
# Script netdiscover.sh.sh
# <25/09/2022> - < Jesus Israel Bolaños Uvalle >

# Escaner de red bàsico en BASH

# Determinado el segmento de red

which ifconfig && { echo "Comando ifconfig existe...";
                    direccion_ip=`ipconfig |grep -w inet | grep -v "127.0.0.1" | awk '{print $2}'`;
                    echo "Esta es tu direccion ip: " $direccion_ip;
                    subred=`ifconfig |grep inet | grep -v "127.0.0.1" | awk '{print $2}'|awk -F. '{print $1","$2","$3","}'`;
                    echo "Esta es tu subred: "$subred;
                    }\
                || { echo "No existe el comando ifconfi...usando ip";
                    direccion_ip=`ip addr show|grep -w inet|grep -v "127.0.0.1"|awk '{print $2}'`;
                    echo "Esta es tu direccion ip: "$direccion_ip;
                    subred=`ip addr show|grep -w inet|grep -v "127.0.0.1"|awk '{ print $2}'|awk -F. '{print $1"."$2"."$3"."}'`;
                    echo " Esta es tu subred: "$subred;
                    }

for ip in {1..254}
do
    ping -q -c 4 ${subred}${ip} > /dev/null
    if [ $? -eq 0 ]
    then
        echo "Host responde: " ${subred}${ip}
    fi
done