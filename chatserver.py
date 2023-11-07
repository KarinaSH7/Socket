"""
Реализовать чат,
который позволит обмениваться сообщениями только между клиентом и сервером.
Клиент должен получать сообщения сервера в том числе. Сигналом окончания связи служит слово "Пока".
"""
import socket


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 55000))
    server_socket.listen(1)

    print("Server is listening on port 55000 ...")

    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established!")

    while True:
        message = client_socket.recv(1024).decode()
        print(f"Client: {message}")
        if message.lower() == "пока":
            break

        response = input("Server: ")
        client_socket.send(response.encode())
        if response.lower() == "пока":
            break

    client_socket.close()


if __name__ == "__main__":
    main()