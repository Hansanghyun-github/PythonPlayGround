import time
import asyncio

async def task(second: int):
    print(f"Task {second} started")
    await asyncio.sleep(second)
    print(f"Task {second} finished")


def test_if_just_call_async_method_then_method_is_not_executed():
    # when
    start = time.time()
    task(1)
    task(2)
    task(3)
    end = time.time()

    # then
    assert end - start < 1
    # execute without await, so it will not be executed

def test_execute_async_method_with_asyncio():
    # when
    start = time.time()
    asyncio.run(task(1))
    asyncio.run(task(2))
    asyncio.run(task(3))
    end = time.time()

    # then
    assert end - start >= 6

def test_execute_async_method_with_asyncio_gather():
    # given
    async def run_all():
        await asyncio.gather(task(1), task(2), task(3))

    # when
    start = time.time()
    asyncio.run(run_all())
    end = time.time()

    # then
    assert 3 <= end - start < 4
