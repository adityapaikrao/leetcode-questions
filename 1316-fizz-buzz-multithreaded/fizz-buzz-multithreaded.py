class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.turn = "number" # one of [number, fizz, buzz, fizzbuzz]
        self.cv = threading.Condition()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        with self.cv:
            for i in range(3, self.n + 1, 3):
                if i % 5 == 0: continue
                while self.turn != "fizz":
                    self.cv.wait()
                printFizz()
                nxt = i + 1
                if nxt % 3 == 0 and nxt % 5 == 0:
                    self.turn = "fizzbuzz"
                elif nxt % 3 == 0:
                    self.turn = "fizz"
                elif nxt % 5 == 0:
                    self.turn = "buzz"
                else:
                    self.turn = "number"
                self.cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        with self.cv:
            for i in range(5, self.n + 1, 5):
                if i % 3 == 0: continue
                while self.turn != "buzz":
                    self.cv.wait()
                printBuzz()
                nxt = i + 1
                if nxt % 3 == 0 and nxt % 5 == 0:
                    self.turn = "fizzbuzz"
                elif nxt % 3 == 0:
                    self.turn = "fizz"
                elif nxt % 5 == 0:
                    self.turn = "buzz"
                else:
                    self.turn = "number"
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        with self.cv:
            for i in range(15, self.n + 1, 15):
                while self.turn != "fizzbuzz":
                    self.cv.wait()
                printFizzBuzz()
                nxt = i + 1
                if nxt % 3 == 0 and nxt % 5 == 0:
                    self.turn = "fizzbuzz"
                elif nxt % 3 == 0:
                    self.turn = "fizz"
                elif nxt % 5 == 0:
                    self.turn = "buzz"
                else:
                    self.turn = "number"
                self.cv.notify_all()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        with self.cv:
            for i in range(1, self.n + 1):
                if i % 3 == 0 or i % 5 == 0: continue
                while self.turn != "number":
                    self.cv.wait()
                
                printNumber(i)
                nxt = i + 1
                if nxt % 3 == 0 and nxt % 5 == 0:
                    self.turn = "fizzbuzz"
                elif nxt % 3 == 0:
                    self.turn = "fizz"
                elif nxt % 5 == 0:
                    self.turn = "buzz"
                else:
                    self.turn = "number"
                self.cv.notify_all()
