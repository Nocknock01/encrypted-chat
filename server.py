import socket
import threading
from crypto_utils import decrypt_message, load_key

key = load_key()
HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            encrypted_message = client.recv(1024)
            message = decrypt_message(encrypted_message, key)
            print("Decrypted:", message)
            broadcast(encrypted_message, client)
        except:
            clients.remove(client)
            client.close()
            break

def receive_connections():
    print("Server is running...")
    while True:
        client, address = server.accept()
        clients.append(client)
        print(f"Connected with {address}")
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
