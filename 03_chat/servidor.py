# Servidor
import socket
import threading

HOST = 'Localhost'
PORT = 9000

clientes = []

def atender_cliente(cliente, nombre):
    while true:
        try:
            mensaje = cliente.recv(1024)
            if not mensaje:
                break
            print(f"{nombre}: {mensaje.decode()}")
            broadcast(mensaje,cliente)
        except connectionResetError:
            clientes.remove(cliente)
            cliente.close()
            break

def broadcast(mensaje, emisor):
    for cliente in clientes:
        if cliente != emisor:
            cliente.sed(mensaje.encode())

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()
print("el servidor 'Chat' esta esperando  conexiones ...")

while True:
    cliente, direccion = servidor.accept()
    print(f"cliente conectado desde la IP {direccion}")
    nombre = cliente.reac(1024).decode()
    clientes,append(cliente)
    broadcast(f"{nombre} se ha unido al 'chat'", cliente)
    hilo_cliente = threading.theread(target=atender_cliente, args=(cliente,nombre))
    hilo_cliente.start()

datos = cliente.recv(1024)
cliente.sendall(b"hola! " + datos) # ojo! debe ser binario, no cadena
cliente.close()
