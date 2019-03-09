import threading
from random import randint
from time import sleep
from utility_mdl import deneme
lock = threading.Lock()


def print_number(number):
    # Sleeps a random 1 to 10 seconds
    lock.acquire()
    rand_int_var = randint(1, 10)
    sleep(3)
    print("Thread " + str(number) + " slept for " + str(3) + " seconds")
    lock.release()


thread_list = []

for i in range(1, 10):
    # Instantiates the thread
    # (i) does not make a sequence, so (i,)
    t = threading.Thread(target=deneme, args=(i,))
    # Sticks the thread in a list so that it remains accessible
    thread_list.append(t)

# Starts threads
for thread in thread_list:
    thread.start()

# This blocks the calling thread until the thread whose join() method is called is terminated.
# From http://docs.python.org/2/library/threading.html#thread-objects
# for thread in thread_list:
#     thread.join()

# Demonstrates that the main process waited for threads to complete
print("Done")