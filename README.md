# 🔐 Encrypted Chat Application (Python)

This is a terminal-based real-time encrypted chat application built using **Python sockets** and the **cryptography** library (Fernet). It allows multiple clients to connect to a server and exchange encrypted messages securely.

---

## 🚀 Features

- 🛡️ End-to-end encrypted communication using Fernet (AES symmetric encryption)
- 💬 Real-time chat between multiple users
- 🧵 Multi-threaded server and client handling
- 🔐 Key generation and storage

---

## 🛠 Requirements

Install dependencies using:

```bash
pip install cryptography

encrypted_chat/
├── server.py              # Chat server
├── client.py              # Chat client
├── crypto_utils.py        # Handles encryption/decryption
├── generate_key.py        # One-time key generator
└── key.key                # Generated encryption key (DO NOT share)
