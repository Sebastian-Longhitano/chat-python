# server.py
"""
Servidor de Chat Mejorado con:
- Manejo elegante de desconexiones
- Logging a archivo .log
- Colores en terminal (Colorama)
"""
import socket
import threading
import logging
from datetime import datetime
from db import init_db, save_message
from colorama import init as colorama_init, Fore, Style

# Inicializar Colorama
colorama_init(autoreset=True)

# Configuración de logging
LOG_FILENAME = 'server.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILENAME),
        logging.StreamHandler()
    ]
)

HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024


def init_socket():
    """Inicializa el socket del servidor."""
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind((HOST, PORT))
    server_sock.listen()
    logging.info(f"Servidor escuchando en {HOST}:{PORT}")
    return server_sock

def handle_client(client_sock, client_addr):
    """Maneja la comunicación con un cliente conectado."""
    logging.info(f"Conexión establecida: {client_addr}")
    try:
        while True:
            data = client_sock.recv(BUFFER_SIZE)
            if not data:
                # Cliente cerró conexión
                logging.info(f"Cliente desconectado: {client_addr}")
                break

            message = data.decode('utf-8').strip()
            # Guardar en DB (timestamp automático en DB)
            save_message(message, client_addr[0])

            # Respuesta al cliente
            response = f"Mensaje recibido: {datetime.now():%Y-%m-%d %H:%M:%S}"
            client_sock.sendall(response.encode('utf-8'))
            print(Fore.GREEN + f"[Enviado a {client_addr}]: " + Style.RESET_ALL + response)

    except ConnectionResetError:
        logging.warning(f"Conexión inesperada terminada por cliente: {client_addr}")
    except Exception as e:
        logging.error(f"Error manejando cliente {client_addr}: {e}")
    finally:
        client_sock.close()
        logging.info(f"Socket cerrado para: {client_addr}")

def main():
    init_db()
    server_sock = init_socket()
    try:
        while True:
            client_sock, client_addr = server_sock.accept()
            thread = threading.Thread(target=handle_client, args=(client_sock, client_addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        logging.info("Servidor detenido por teclado.")
    finally:
        server_sock.close()
        logging.info("Socket del servidor cerrado.")

if __name__ == '__main__':
    main()
