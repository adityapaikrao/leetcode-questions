import threading
class H2O:
    def __init__(self):
        # pass
        self.hydrogen_sema = threading.BoundedSemaphore(2)
        self.oxygen_sema = threading.Semaphore(0)

        self.oxygen_lock = threading.Lock()
  

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.hydrogen_sema.acquire()
        releaseHydrogen()
        self.oxygen_sema.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.oxygen_lock:
            self.oxygen_sema.acquire()
            self.oxygen_sema.acquire()  
        releaseOxygen()
        self.hydrogen_sema.release(2)