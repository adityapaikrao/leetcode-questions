class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = threading.Lock()
        self.barLock = threading.Lock()
        self.barLock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):

            # printFoo() outputs "foo". Do not change or remove this line.
            self.fooLock.acquire()
            printFoo()
            self.barLock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            self.barLock.acquire()
            printBar()
            self.fooLock.release()