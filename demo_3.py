from threading import Thread
from queue import Queue
from urllib.request import urlopen
from time import time

sira = Queue()

siteler = ("http://www.python.org",
           "http://istihza.com",
           "http://yasararabaci.tumblr.com",
           "http://metehan.us",
           "http://blog.tanshaydar.com",
           "http://fatihmertdogancan.wordpress.com",
           "http://ozgurerdogdu.blogspot.com/")


def siteokuyan(que):
    while True:
        site = que.get()
        f = urlopen(site)
        _ = f.read()
        f.close()
        que.task_done()


if __name__ == "__main__":
    basla = time()
    # 5 thread olustur;
    for i in range(5):
        t = Thread(target = siteokuyan, args = (sira,))
        t.daemon = True
        t.start()

    # sitelerimizi siraya ekleyelim;
    for site in siteler:
        sira.put(site)

    # siranin bosalmasini bekle
    sira.join()
    print("%s saniye surdu" % (time() - basla))