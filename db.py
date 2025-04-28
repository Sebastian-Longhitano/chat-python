# db.py
"""
Módulo de Base de Datos
"""
import sqlite3
import logging

DB_NAME = 'mensajes.db'

# Logger para la base de datos
db_logger = logging.getLogger('db')

def init_db():
    """Crea la tabla con timestamp automático si no existe."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensajes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            fecha_envio DATETIME DEFAULT CURRENT_TIMESTAMP,
            ip_cliente TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    db_logger.info("Tabla 'mensajes' creada.")

def save_message(contenido, ip_cliente):
    """Inserta mensaje; fecha se gestiona en la DB."""
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mensajes (contenido, ip_cliente) VALUES (?, ?)",
            (contenido, ip_cliente)
        )
        conn.commit()
        conn.close()
        db_logger.info(f"Mensaje guardado de {ip_cliente}")
    except sqlite3.Error as e:
        db_logger.error(f"Error guardando mensaje: {e}")