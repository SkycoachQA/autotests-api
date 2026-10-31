import asyncio


async def fetch_data():
    print("Начинаем загрузку...")
    await asyncio.sleep(2)
    print("Данные загружены")
    return {"data": "Пример данных"}


async def main():
    result = await fetch_data()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
