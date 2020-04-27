import time
from concurrent.futures import ThreadPoolExecutor

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


with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(greet)
    pool.submit(calculate)

#pool.shutdown()
