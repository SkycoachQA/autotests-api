from concurrent import futures
import socket


def handle_client(client_socket, client_address, messages):
    try:
        print(f"Пользователь с адресом: {client_address} подключился к серверу")
        message = client_socket.recv(1024).decode()
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {message}")
        messages.append(message)
        client_socket.sendall("\n".join(messages).encode())
    finally:
        client_socket.close()


def server():
    messages = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("localhost", 12345))
        server_socket.listen(10)
        print("TCP сервер пользователей запущен на localhost:12345")
        with futures.ThreadPoolExecutor(max_workers=10) as executor:
            while True:
                client_socket, client_address = server_socket.accept()
                executor.submit(handle_client, client_socket, client_address, messages)


if __name__ == "__main__":
    server()
