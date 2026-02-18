# Cliente
import socket
import threading

HOST = 'localhost'
PORT = 9000

def recibir_mensajes(cliente):
    while True:
        mensaje = cliente.recv(1024).decode()
        print(mensaje)


nombre = input("ingrese su nombre: ")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
cliente.sendall(nombre.encode())

hilo_recibir = threading.Thread(target = recibir_mensajes, args =(cliente,))
hilo_recibir.start()

while True:
    mensaje = input("Mensaje: ")
    cliente.send(mensaje.encode())

cliente.sendall(b"Mundo!")
respuesta = cliente.recv(1024)
print(f"respuesta del servidor: {respuesta.decode()}")

cliente.close()
