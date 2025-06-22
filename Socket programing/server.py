import socket

# socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1' #local machine IP address
port = 12345 #port no.

# Port binding
server_socket.bind((host, port))

# Wait for client connection 
server_socket.listen(1)
print(f"Server listening on {host}:{port}...")

# Accept connection
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data or data.lower() == 'exit':
        print("Connection closed.")
        break
    print(f"Client: {data}")
    reply = input("You (Server): ")
    conn.send(reply.encode())
    if reply.lower() == 'exit':
        print("Server exited the chat.")
        break

conn.close()
