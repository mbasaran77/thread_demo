from threading import Thread
from random import randint
from time import sleep

def basvuru(basvuru_id):
    sleep(randint(0, 60))
    if randint(0, 1):
        print("başvuru  kabul edildi", basvuru_id)
    else:
        print("başvuru reddedildi", basvuru_id)


for i in range(5):
    Thread(target=basvuru, args=(i, )).start()
