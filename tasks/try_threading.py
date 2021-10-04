import threading
import time


def m1():
    print("Hello. I am m1")
    time.sleep(10)
    print("Bye from m1")

def m2():
    print("Hello. I am m2")
    time.sleep(2)
    print("Bye from m2")


t1 = threading.Thread(target=m1)
t2 = threading.Thread(target=m2)

t1.start()
t2.start()

t1.join()
t2.join()


# m1()
# m2()
