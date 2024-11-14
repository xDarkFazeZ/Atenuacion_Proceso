import socket
import time

PRIMARY_SERVER = ("127.0.0.1", 8000)  # Java server
BACKUP_SERVER = ("127.0.0.1", 8001)   # Python server

def check_server(server_address):
    """Verifica la disponibilidad de un servidor sin enviar datos."""
    try:
        with socket.create_connection(server_address, timeout=2) as sock:
            response = sock.recv(1024)  # Espera recibir el mensaje
            if response:
                print(f"Respuesta del servidor {server_address[1]}: {response.decode()}")
                return True
    except (socket.timeout, ConnectionRefusedError, ConnectionAbortedError) as e:
        print(f"Error en la conexión con el servidor {server_address[1]}: {e}")
        return False

def main_client():
    current_server = PRIMARY_SERVER
    while True:
        if check_server(current_server):
            print(f"Conectado al servidor en el puerto {current_server[1]}")
            time.sleep(5)  # Espera antes de volver a verificar
        else:
            print(f"Servidor en el puerto {current_server[1]} no disponible.")
            # Cambia al servidor de respaldo
            if current_server == PRIMARY_SERVER:
                print("Intentando conectar al servidor de respaldo...")
                current_server = BACKUP_SERVER
            else:
                # Si también falla el servidor de respaldo, se espera un momento y vuelve a intentar.
                print("Ambos servidores están inactivos, intentando nuevamente en 10 segundos...")
                current_server = PRIMARY_SERVER
                time.sleep(10)

if __name__ == "__main__":
    main_client()
