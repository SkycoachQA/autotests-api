import asyncio

import websockets
from websockets import ServerConnection


async def handle_user(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        for number in range(1, 6):
            await websocket.send(f"{number} Сообщение пользователя: {message}")


async def main():
    server = await websockets.serve(handle_user, "localhost", 8765)
    print("WebSocket сервер пользователей запущен на ws://localhost:8765")
    await server.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
