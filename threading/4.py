import time
from concurrent.futures import ProcessPoolExecutor

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

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(greet)
    pool.submit(calculate)


