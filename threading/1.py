import time
from threading import Thread

def greet():
    start = time.time()
    name = input("Enter your name: ")
    print(f"Hello {name}")
    print(f"greet ran in {time.time()-start} seconds")

def calculate():
    start = time.time()
    [x**2 for x in range(20000000)]
    print(f"calculate ran in {time.time()-start} seconds")

start = time.time()
greet()
calculate()
print(f"The single thread execution took {time.time()-start} seconds")

thread1 = Thread(target=greet)
thread2 = Thread(target=calculate)

start = time.time()

thread2.start()
thread1.start()

thread1.join()
thread2.join()

print(f"The two threded execution took {time.time()-start} seconds")
