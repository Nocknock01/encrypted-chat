import socket
import threading
from crypto_utils import encrypt_message, decrypt_message, load_key

key = load_key()
HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            encrypted_message = client.recv(1024)
            message = decrypt_message(encrypted_message, key)
            print("\n[Received]:", message)
        except:
            print("Connection closed.")
            client.close()
            break

def send_messages():
    while True:
        message = input("[you]: ")
        encrypted_message = encrypt_message(message, key)
        client.send(encrypted_message)

threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
