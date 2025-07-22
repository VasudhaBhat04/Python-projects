import socket

# socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1' 
port = 12345

# Connect to the server
client_socket.connect((host, port))
print(f"Connected to server at {host}:{port}")

while True:
    message = input("You (Client): ")
    client_socket.send(message.encode())
    if message.lower() == 'exit':
        print("Client exited the chat.")
        break
    reply = client_socket.recv(1024).decode()
    if not reply or reply.lower() == 'exit':
        print("Server closed the chat.")
        break
    print(f"Server: {reply}")

#close socket
client_socket.close()
