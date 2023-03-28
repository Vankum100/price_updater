import asyncio
import threading


def set_timeout(callback, delay, *args, **kwargs):
    t = threading.Timer(delay / 1000, callback, args, kwargs)
    t.start()
    return t


def set_interval(callback, interval, *args, **kwargs):
    stopped = threading.Event()

    def loop():
        while not stopped.wait(interval / 1000):
            callback(*args, **kwargs)

    t = threading.Thread(target=loop)
    t.start()
    return stopped.set


def clear_interval(timer):
    timer.set()


def clear_timeout(timer):
    timer.cancel()


async def set_timeout_async(callback, delay, *args, **kwargs):
    await asyncio.sleep(delay / 1000)
    await callback(*args, **kwargs)


def clear_timeout_async(timer_id):
    timer_id.cancel()


async def set_interval_async(callback, interval, *args, **kwargs):
    while True:
        await asyncio.sleep(interval / 1000)
        await callback(*args, **kwargs)


def clear_interval_async(timer_id):
    timer_id.cancel()
