import time
import threading

def printTest1():
    print ("Hello, from print 1")
    time.sleep(1)
    print ("Goodbye, from print 1")

def printTest2():
    print ("Hello, from print 2")
    time.sleep(1)
    print ("Goodbye, from print 2")

thread1 = threading.Thread(target=printTest1)
thread2 = threading.Thread(target=printTest2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
