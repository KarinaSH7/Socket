import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 55000))

    filename = input("Enter the filename: ")
    client_socket.send(filename.encode())

    word_count = client_socket.recv(55000).decode()
    print(f"The file contains {word_count} words.")

    client_socket.close()


if __name__ == "__main__":
    main()