import requests
import json

#Nombre: Jesus Israel Bolaños Uvalle
#Matricula: 2005587

if __name__ == "__main__":
    url ="https://httpbin.org/post"
    argumentos = {"nombre": "Israel", "matricula": "2005587", "curso":"Laboratorio de Programacion para Ciberseguridad"}

    response = requests.post(url, params=argumentos)

    if response.status_code == 200:
        print(response.content)
