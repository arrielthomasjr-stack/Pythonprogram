from threading import Thread
from queue import Queue
import time

buffer = Queue(maxsize=5)        # bounded buffer of size 5

def producer():
    for i in range(10):
        buffer.put(i)               # blocks if buffer is full
        print(f"+ produced {i}")
        time.sleep(0.10)

def consumer():
    for _ in range(10):
        x = buffer.get()              # blocks if buffer is empty
        print(f"-  consumed {x}")
        time.sleep(0.30)            # slower than producer

p = Thread(target=producer); c = Thread(target=consumer)
p.start(); c.start()
p.join();  c.join()