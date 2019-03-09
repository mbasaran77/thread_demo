import threading
from time import sleep


lock = threading.Lock()

def deneme(number):
    # Sleeps a random 1 to 10 seconds
    lock.acquire()
    sleep(3)
    print("Thread " + str(number) + " slept for " + str(3) + " seconds")
    lock.release()


class sayac():
    d2 = 0

    def __init__(self):
        self.d1  = 0
        self.cls_metd()

    def get(self):
        return self.d1

    @classmethod
    def cls_metd(cls):
        cls.d2 += 1
        return cls.d2

if __name__ == '__main__':
    s1 = sayac()
    s2 = sayac()
    s3 = sayac()
    print(s1.get())
    print(s2.get())
    print(s1.d2)
    print(s2.d2)
    print(s3.d2)
    # print(s1.d1)
    # print(s2.d1)
