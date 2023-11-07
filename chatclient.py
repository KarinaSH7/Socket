import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 55000))

    while True:
        message = input("Client: ")
        client_socket.send(message.encode())
        if message.lower() == "пока":
            break

        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")
        if response.lower() == "пока":
            break

    client_socket.close()


if __name__ == "__main__":
    main()