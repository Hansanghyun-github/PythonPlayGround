import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(2)  # 2초 대기 (비동기적으로)
    print("World!")

async def say_hi():
    print("Hi!")
    await asyncio.sleep(1)  # 1초 대기 (비동기적으로)
    print("Python!")

async def main():
    await asyncio.gather(say_hello(), say_hi())

asyncio.run(main())
print("End of Program")