import threading
import time
def tråd1(tall, tall2):
    while True:
        print(tall, tall2)
        time.sleep(2)

def tråd2():
    while True:
        print("Tråd 2 kjører")
        time.sleep(2)

t1 = threading.Thread(target=tråd1, args=(1,18))
t2 = threading.Thread(target=tråd2)
t1.start()
t2.start()