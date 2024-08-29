import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen()

clients = []
names = []

def broadcast(msg):
    for client  in clients:
        client.send(msg)

def client_connection(client):

    while(True):

        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            broadcast(f'{name} left the chat! '.encode('ascii'))
            names.remove(name)
            break

def receive():

    while(True):

        client,address = server.accept()
        print(f'connected with {str(address)}')

        client.send('NICK'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        names.append(name)
        clients.append(client)

        print(f'Name of the client is: {name}')
        broadcast(f'{name} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=client_connection, args=(client,))
        thread.start()

print('Server is listening.....')

receive()