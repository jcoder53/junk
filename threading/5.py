#The purpose of this program is to illustarte the problem of multithreading with shared resouces. If you uncomment all the sleep statements, you can see a messed output. This is bcoz the threads access the global variable counter randomly.

import random
import time
from threading import Thread

counter = 0

def incrementor():
    global counter
    #time.sleep(random.random())
    counter += 1
    #time.sleep(random.random())
    print(f"New counter = {counter}")


for i in range(10):
    t = Thread(target=incrementor)
    #time.sleep(random.random())
    t.start()

