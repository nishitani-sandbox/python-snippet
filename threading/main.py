import threading
import time
import queue

def double_with_sleep(q, i):
    time.sleep(3)
    q.put(i * 2)

def main():
    q = queue.Queue()
    threads = []
    for i in range(5):
        t = threading.Thread(target=double_with_sleep, args=(q, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(q.get())

main()
