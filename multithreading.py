#remove hash to run the code differently
import threading
#threadLock=threading.Lock()
class Thread1(threading.Thread):
    def run(self):
        #lock.acquire()
        i=1
        while(i<=10):
            print(i,end='\n')
            i=i+1
        #lock.release()    
t=Thread1()
t1=Thread1()
t.start()
t1.start()

t.join()
i=1
while(i<=10):
    print(i,end='\n')
    i=i+1
    
