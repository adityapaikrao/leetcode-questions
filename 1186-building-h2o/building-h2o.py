class H2O:
    def __init__(self):
        self.barrier = threading.Barrier(3)
        self.hydrogen_sema = threading.Semaphore(2)
        self.oxygen_sema = threading.Semaphore(1)
        
    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.hydrogen_sema.acquire()
        self.barrier.wait()
        releaseHydrogen()
        self.hydrogen_sema.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.oxygen_sema.acquire()
        self.barrier.wait()
        releaseOxygen()
        self.oxygen_sema.release()