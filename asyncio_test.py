#Date:2018-12-10
#Author:Thomson

from threading import Thread,currentThread
import time

#阻塞检测，一个线程阻塞，另一个线程执行
def do_something(x):
    time.sleep(x)
    print(time.ctime())

thread1 = Thread(target=do_something,args=(1,))
thread2 = Thread(target=do_something,args=(2,))
thread3 = Thread(target=do_something,args=(3,))
thread4 = Thread(target=do_something,args=(4,))
thread5 = Thread(target=do_something,args=(5,))

threads = []
threads.append(thread1)
threads.append(thread4)
threads.append(thread3)
threads.append(thread2)
threads.append(thread5)

for thread in threads:
    thread.start()


#共有数据的争夺检测
start = time.time()

def do_something(x):
    global a
    time.sleep(x)
    for b in range(1,51):   #计算从1+...+50
        a+=b
    print(currentThread(),":",a)

a = 0
threads = []

for i in  range(1,20000):
   thread = Thread(target=do_something,args=(1,))
   threads.append(thread)


for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.time()
print(end-start)

import asyncio
import time

a = 0
tasks = []
num = 0

start = time.time()

# 密集运算测试
async def do_something(x):
    global a
    global num
    #num += 1          #num自增的位置（在阻塞前/后）不同会产生不同的结果
    await asyncio.sleep(x)
    for b in range(1,51):   #计算从1+...+50
        a+=b
    num += 1
    print("this is coroutetime",":",x,a)

for i in range(1,20000):
    coroutine = do_something(1)  #即使睡眠的时间很短，运算量大都不会产生资源争夺
    #coroutine = do_something(i*0.01)
    tasks.append(asyncio.ensure_future(coroutine))

loop = asyncio.get_event_loop()  #创建事件循环
loop.run_until_complete(asyncio.wait(tasks))  #将协程塞进事件循环中

end = time.time()

print(end-start)



