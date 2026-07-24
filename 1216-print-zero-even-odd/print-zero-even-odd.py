from threading import Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cv = Condition()
        self.turn = 0 # (0, 1, 2) -> 0, odd, even
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            with self.cv:
                while self.turn != 0:
                    self.cv.wait()
                printNumber(0)
                if i % 2 == 0:
                    self.turn = 1
                else:
                    self.turn = 2
                self.cv.notify_all()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            with self.cv:
                while self.turn != 2:
                    self.cv.wait()
                printNumber(i)
                self.turn = 0
                self.cv.notify_all()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            with self.cv:
                while self.turn != 1:
                    self.cv.wait()
                printNumber(i)
                self.turn = 0
                self.cv.notify_all()
        