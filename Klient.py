import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.1.59", 8888))

    while True:
        command = input("Enter command (Random/Add/Subtract): ")
        if command not in ["Random", "Add", "Subtract"]:
            print("Invalid command")
            continue

        param1 = input("Enter first number: ")
        param2 = input("Enter second number: ")

        request = f"{command};{param1};{param2}"
        client.send(request.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print("Server response:", response)

if __name__ == "__main__":
    main()
