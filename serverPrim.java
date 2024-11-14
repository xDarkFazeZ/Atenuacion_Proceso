import java.io.*;
import java.net.*;

public class serverPrim { // Cambié el nombre de la clase a mayúscula inicial (convención Java)
    private int port;

    public serverPrim(int port) {
        this.port = port;
    }

    public void start() {
        try (ServerSocket serverSocket = new ServerSocket(port, 50, InetAddress.getByName("192.168.0.211"))) { // Cambié la IP a localhost
            System.out.println("Servidor escuchando en la dirección 192.168.0.211 y el puerto " + port);

            while (true) {
                try (Socket clientSocket = serverSocket.accept()) {
                    System.out.println("Conexión desde " + clientSocket.getInetAddress());

                    OutputStream out = clientSocket.getOutputStream();
                    out.write("Hola desde el servidor 1 de Java!\n".getBytes());
                    out.flush();
                } catch (IOException e) {
                    System.out.println("Error al comunicar con el cliente: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.out.println("No se puede iniciar el servidor en la dirección y el puerto especificados.");
        }
    }

    public static void main(String[] args) {
        int port = 8000; // Cambia a 8001 para el servidor de respaldo
        serverPrim server = new serverPrim(port); // Cambié el nombre de la clase aquí también
        server.start();
    }
}
