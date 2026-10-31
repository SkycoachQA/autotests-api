import socket


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("localhost", 12345))
        client_socket.sendall("Привет, сервер!".encode())
        chunks = []
        while True:
            chunk = client_socket.recv(1024)
            if not chunk:
                break
            chunks.append(chunk)
        print(b"".join(chunks).decode())


if __name__ == "__main__":
    client()
