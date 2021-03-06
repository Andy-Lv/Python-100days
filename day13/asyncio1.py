"""
异步I/O操作 - asyncio模块
"""

import asyncio2
import threading

@asyncio2.coroutines
def hello():
    print('%s: hello, world!' % threading.current_thread())
    # 休眠不会阻塞主线程因为使用了异步I/O操作
    # 注意有yield from才会等待休眠操作执行完成
    yield from asyncio2.sleep(2)
    # asyncio.sleep(1)
    # time.sleep(1)
    print('%s: goodbye, world!' % threading.current_thread())


loop=asyncio2.get_event_loop()
task=[hello(),hello()]
loop.run_until_complete(asyncio2.wait(tasks))
print('game over!')
loop.close()