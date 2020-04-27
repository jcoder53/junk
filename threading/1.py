import time
from threading import Thread

def greet():
    start = time.time()
    name = input("Enter your name: ")
    print(f"Hello {name}")
    print(f"Time taken for greet: {time.time()-start}")

def calculate():
    start = time.time()
    print("Start calculating...")
    [x**2 for x in range(20000000)]
    print(f"Time taken for calculate: {time.time()-start}")

start = time.time()
#greet()
calculate()
calculate()
print(f"Total time taken is {time.time()-start}")

thread1 = Thread(target=calculate)
thread2 = Thread(target=calculate)

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(f"Time taken for two threaded: {time.time()-start}")
