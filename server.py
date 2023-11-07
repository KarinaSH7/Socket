import socket


def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return -1


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 55000))
    server_socket.listen(1)

    print("Server is listening on port 55000...")

    client_socket, address = server_socket.accept()
    print(f"Connection from {address} has been established!")

    filename = client_socket.recv(1024).decode()
    print(f"Received filename: {filename}")

    word_count = count_words(filename)
    client_socket.send(str(word_count).encode())

    client_socket.close()


if __name__ == "__main__":
    main()