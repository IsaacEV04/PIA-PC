# Nombre: Isaac Emilio Esparza Vázquez
# Matrícula: 2012872
import requests
import json


if __name__ == "__main__":
    url ="https://httpbin.org/post"
    argumentos = {"nombre": "Isaac", "matricula": "2012872", "curso":"Programacion para Ciberseguridad"}

    response = requests.post(url, params=argumentos)

    if response.status_code == 200:
        print(response.content)
