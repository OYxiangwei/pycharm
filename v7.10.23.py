import asyncio
import threading
async def sum(a,b):
    print(threading.current_thread())
    r = a+b
    await asyncio.sleep(1)
    print(threading.current_thread())
    print(r)
    return r
loop = asyncio.get_event_loop()
#task = [sum(1,2),sum(2,3),sum(3,9)]
task = asyncio.gather(sum(1,2),sum(2,3),sum(4,3))
loop.run_until_complete(task)
r1,r2,r3 = task.result()
print(r1,r2,r3)
loop.close()