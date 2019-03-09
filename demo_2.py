from time import sleep
from threading import Thread


def tekrarla(ne, bekleme):
    # while True:
    print(ne)
    sleep(bekleme)
    print("bekleme : ", ne)


if __name__ == '__main__':
    dum = Thread(target=tekrarla, args=("dum", 1))
    this = Thread(target=tekrarla, args=("this", 0.5))
    ah = Thread(target=tekrarla, args=("ah", 3))

    dum.start()
    this.start()
    ah.start()
    # dum.join()
    # this.join()
    # ah.join()