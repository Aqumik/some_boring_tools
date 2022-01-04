import threading
import sys
import time

#https://ithelp.ithome.com.tw/articles/10254439
def socket1():
    # for i in range(1,6):
    lock_s2.acquire()
    print('socket-server1')
    lock_s1.release()
    time.sleep(0.1)


def socket2():
    # for i in range(1,6):
    lock_s1.acquire()
    print('socket-server2')
    lock_s2.release()
    time.sleep(0.1)


if __name__ == "__main__":
    lock_s1 = threading.Lock()
    lock_s2 = threading.Lock()

    t1 = threading.Thread(None,socket1())
    t2 = threading.Thread(None,socket2())
    lock_s1.acquire()
    t1.start()
    t2.start()
    t1.join()