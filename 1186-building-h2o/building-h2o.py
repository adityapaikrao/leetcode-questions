class H2O:
    def __init__(self):
        self.cv = threading.Condition()
        self.numH = 0
        self.numO = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        with self.cv:
            while self.numH == 2:
                self.cv.wait()
            
            self.numH += 1
            releaseHydrogen()

            if self.numH == 2 and self.numO == 1:
                self.numH, self.numO = 0, 0
            self.cv.notify_all()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.cv:
            while self.numO == 1:
                self.cv.wait()

            self.numO += 1
            releaseOxygen()
            
            if self.numH == 2 and self.numO == 1:
                self.numH, self.numO = 0, 0
            self.cv.notify_all()
