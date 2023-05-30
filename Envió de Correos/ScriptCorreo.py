#Jesús Israel Bolaños Uvalle
#2005587

import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#Le asignamos el asunto, de quien y para quien va dirigido el correo
mensaje = MIMEMultipart('alternative')
mensaje['Subject'] = 'Prueba de envio (script Python) - 2005587'
mensaje['From'] = 'correo'
mensaje['To'] = 'destinatario'

html = f"""
<html>
<body>
    <b>Practica 12</b><br>
    Ejercicio de la practica 12 para envio de correos.<br>
    <b>Alumno:</b> Jesús Israel Bolaños Uvalle<br>
    <b>Matrícula:</b> 2005587<br>
<body>
</html>
"""
#Agregamos el html al contenido del mensaje
parte_html = MIMEText(html, 'html')
mensaje.attach(parte_html)

#Abrimos la imagen, la leeamos para luego adjuntarlo al mensaej final              
imagen= "fcfm_cool.png"

with open(imagen, 'rb') as adjunto:
    contenido_adjunto =MIMEBase("application", "octet-stream")
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)

contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename= {imagen}",
)


mensaje.attach(contenido_adjunto)
mensaje_final = mensaje.as_string()

context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', 587) as conn:
    conn.starttls(context=context)
    conn.login('correo', 'contraseña')
    print("Sesión iniciada")
    conn.sendmail('correo', 'destinatario', mensaje_final)
    print("Mensaje enviado")

