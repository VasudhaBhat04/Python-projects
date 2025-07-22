import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '10.24.125.214'  # Replace with your server's IP address
    server_port = 5050
    server_socket.bind((server_ip, server_port))  # Bind to the server's IP and port
    server_socket.listen(1)
    print(f"Server running on {server_ip}:{server_port}")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    conn.sendall(b"Welcome to the server!")
    conn.close()

start_server()