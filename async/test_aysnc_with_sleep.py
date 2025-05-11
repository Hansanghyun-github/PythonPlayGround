import time
import asyncio

async def task_with_sleep(second: int):
    print(f"Task {second} started")
    time.sleep(second)
    print(f"Task {second} finished")

def test_execute_async_method_with_sleep():
    # given
    async def run_all():
        await asyncio.gather(task_with_sleep(1), task_with_sleep(2), task_with_sleep(3))

    # when
    start = time.time()
    asyncio.run(run_all())
    end = time.time()

    # then
    assert end - start >= 6
    # sleep is blocking the thread, so it will not be executed in parallel
