from cryptography.fernet import Fernet

# Generate and save a key once
def generate_key():
    return Fernet.generate_key()

# Save the key to a file
def save_key(key, filename='key.key'):
    with open(filename, 'wb') as f:
        f.write(key)

# Load the key from a file
def load_key(filename='key.key'):
    with open(filename, 'rb') as f:
        return f.read()

# Encrypt message
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

# Decrypt message
def decrypt_message(message, key):
    f = Fernet(key)
    return f.decrypt(message).decode()
