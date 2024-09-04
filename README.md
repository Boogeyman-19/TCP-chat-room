# TCP Chat Room in Python

This is a Python implementation of a simple TCP-based chat room. Multiple clients can connect to the server and exchange messages in real-time. The server handles client connections and broadcasts messages to all connected clients.

## Features

- **Multi-client support**: The server can handle multiple clients simultaneously.
- **Broadcast messaging**: Messages from one client are broadcast to all connected clients.
- **Simple text-based chat**: A basic text interface for chatting between clients.

## Requirements

- Python 3.x

No additional external libraries are required.

## How It Works

1. **Server**: The server listens for incoming client connections. When a client connects, the server spawns a new thread to handle the communication with that client. The server broadcasts any message received from a client to all other connected clients.

2. **Client**: The client connects to the server using its IP address and port. After connecting, the client can send messages to the server, which are then broadcast to all other clients.

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/Boogeyman-19/tcp-chat-room.git
cd tcp-chat-room
```

### 2. Start the server

Run the server script to start the chat room server. The server will listen for client connections on a specified IP and port.

```bash
python server.py
```

By default, the server listens on `localhost` and port `12345`. You can change these values in the code if needed.

### 3. Start the client(s)

Open a new terminal window or tab and run the client script to connect to the server. You can run multiple clients to simulate a multi-user chat room.

```bash
python client.py
```

The client will prompt you to enter your username, which will be used to identify you in the chat room.

### Example Usage

1. Start the server:
   ```bash
   python server.py
   ```
   Server running on `localhost:12345`.

2. Start a client:
   ```bash
   python client.py
   ```
   Enter your username and start chatting!

## Project Structure

- `server.py`: The server-side code that handles client connections and message broadcasting.
- `client.py`: The client-side code that connects to the server and handles sending/receiving messages.

## Customization

You can customize the following parameters in the code:

- **Server IP and Port**: Change the IP address and port on which the server listens.
- **Buffer size**: Adjust the buffer size for receiving messages (default is 1024 bytes).

## Known Issues

- No authentication: This is a simple chat room, and there is no authentication mechanism in place.
- Basic error handling: The implementation includes basic error handling but may need improvements for production use.


## Contributions

Feel free to contribute to the project by submitting a pull request or opening an issue.

---

