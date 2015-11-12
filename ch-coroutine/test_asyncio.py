# -*- coding: utf-8 -*-
import asyncio
import threading
__author__ = 'PCPC'


@asyncio.coroutine
def hello():
    print('hello world (%s)'% threading.current_thread())
    r = yield from  asyncio.sleep(1)
    print('hello again! (%s)'%threading.current_thread() )


loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()