import  threading
import sys
import time


def showa():
    while True:
        lockc.acquire()
        print('a',end='')
        sys.stdout.flush()
        locka.release()
        time.sleep(0.2)

def showb():
    while True:
        locka.acquire()
        print('b',end='')
        sys.stdout.flush()
        lockb.release()
        time.sleep(0.2)

def showc():
    while True:
        lockb.acquire()
        print('c',end='')
        sys.stdout.flush()
        lockc.release()
        time.sleep(0.2)

if __name__=='__main__':
    locka = threading.Lock()
    lockb = threading.Lock()
    lockc = threading.Lock()

    t1 = threading.Thread(target=showa)
    t2 = threading.Thread(target=showb)
    t3 = threading.Thread(target=showc)

    locka.acquire()
    lockb.acquire()

    t1.start()
    t2.start()
    t3.start()