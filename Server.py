import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
clients = {}

def acceptconnectionns():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(clients.addr)

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")

    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print("\t\t\t\t\tSERVER IS WAITINNG FOR INCOMMING  CONNECTIONS....")
    print("\n")

    acceptconnectionns()

setup_thread = Thread(target = setup)
setup_thread.start()
