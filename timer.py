from time import *
from threading import *
from random import randint

def show_time(thread):
    print(strftime(str(thread) + ": %m/%d/%Y %H:%M:%S"))
          
def thread_func(thread):
    wait_time = randint(1, 5)
    while (True):
        show_time(thread)
        sleep(wait_time)
        
def main():
    threads = []
    
    for i in range(4):
        threads.append(Thread(target=thread_func, args=[i]))
        threads[i].start()
        
if __name__ == '__main__':
    main()
