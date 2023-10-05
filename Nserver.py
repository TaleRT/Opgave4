import socket
import random
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    command, param1, param2 = request.split(';')

    if command == "Random":
        result = str(random.randint(int(param1), int(param2)))
    elif command == "Add":
        result = str(int(param1) + int(param2))
    elif command == "Subtract":
        result = str(int(param1) - int(param2))
    else:
        result = "Invalid command"

    client_socket.send(result.encode('utf-8'))
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.59", 8888))
    server.listen(5)
    print("Server listening on port 8888")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
