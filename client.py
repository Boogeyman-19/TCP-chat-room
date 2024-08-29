import socket
import threading
import os

# Get server address and port from environment variables
SERVER_HOST = os.getenv('SERVER_HOST', 'localhost')
SERVER_PORT = int(os.getenv('SERVER_PORT', 9999))

name = input('Enter your name: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((SERVER_HOST, SERVER_PORT))
except Exception as e:
    print(f"Unable to connect to the server: {e}")
    exit()

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('ascii')
            if msg == 'NICK':
                client.send(name.encode('ascii'))
            else:
                print(msg)
        except Exception as e:
            print(f"An error occurred: {e}")
            client.close()
            break

def write():
    while True:
        msg = f'{name}: {input("")}'
        try:
            client.send(msg.encode('ascii'))
        except Exception as e:
            print(f"An error occurred while sending the message: {e}")
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
