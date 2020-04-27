#ALERT:This code won't work bcoz of "EOFError: EOF when reading a line". The problem is the second process cannot run the input function as it doesn't have access to the console bcoz resource sharing is not easy in multiprocessing. It would have worked if it doesn't require resource sharing.


import time
from multiprocessing import Process

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

process = Process(target=calculate)
process2 = Process(target=greet)

start = time.time()

process.start()
process2.start()

print(f"The two process execution took {time.time()-start} seconds")

