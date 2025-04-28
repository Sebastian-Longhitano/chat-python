# client.py
"""
Cliente de chat en Python
"""
import socket
import logging
from colorama import init as colorama_init, Fore, Style

# Inicializar Colorama
colorama_init(autoreset=True)

# Logging de cliente
LOG_FILE = 'client.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024
EXIT_COMMANDS = ('exit', 'salir')

def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        logging.info(f"Conectado a {HOST}:{PORT}")

        while True:
            msg = input(Fore.CYAN + "Tu mensaje (exit/salir para salir): " + Style.RESET_ALL).strip()
            if msg.lower() in EXIT_COMMANDS:
                logging.info("Cerrando conexión de cliente.")
                break
            if not msg:
                print(Fore.YELLOW + "No se envían mensajes vacíos." + Style.RESET_ALL)
                continue

            sock.sendall(msg.encode('utf-8'))
            data = sock.recv(BUFFER_SIZE)
            if not data:
                logging.warning("Servidor cerró la conexión.")
                break

            response = data.decode('utf-8')
            print(Fore.GREEN + "Servidor:" + Style.RESET_ALL, response)

    except ConnectionRefusedError:
        logging.error("No se pudo conectar al servidor.")
    except Exception as e:
        logging.error(f"Error en cliente: {e}")
    finally:
        sock.close()
        logging.info("Socket cliente cerrado.")

if __name__ == '__main__':
    main()