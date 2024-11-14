import socket

def start_python_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Servidor Python escuchando en {host}:{port}")
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexión desde {addr}")
        client_socket.send(b"Hola desde el servidor 2 de Python!")
        client_socket.close()

# Ejecuta el servidor en localhost en el puerto 8001
if __name__ == "__main__":
    start_python_server("192.168.0.211", 8001)
