# Chat Básico Cliente-Servidor con Sockets y Base de Datos

## ¿Qué hace la aplicación?
Este proyecto implementa un sencillo servicio cliente-servidor en Python que permite:
- Enviar mensajes desde un cliente TCP al servidor.
- El servidor guarda cada mensaje en una base de datos SQLite (`mensajes.db`).
- El servidor responde al cliente con una confirmación y la fecha/hora de recepción.
- Tanto cliente como servidor registran eventos y errores en archivos de log.

## Instalación (Windows)
1. Asegúrate de tener Python 3.7 o superior instalado.
2. Abre una ventana de **CMD** en la carpeta del proyecto.
3. Crea un entorno virtual con el CMD de Windows:
   python -m venv venv

## Instrucciones de uso
1. Activa el entorno virtual:  venv\Scripts\activate
2. Iniciar el servidor en una terminal de VSC: python server.py
3. Iniciar el cliente en una terminal de VSC: python client.py

## ¿Dónde se guardan los archivos?
- Logs del servidor: server.log en la carpeta del proyecto.
- Logs del cliente: client.log en la carpeta del proyecto.
- Base de datos de mensajes: mensajes.db en la carpeta del proyecto.
