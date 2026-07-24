class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_ = True
        self.cv = threading.Condition()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):

            # printFoo() outputs "foo". Do not change or remove this line.
            with self.cv:
                while not self.foo_:
                    self.cv.wait()
    
                printFoo()
                self.foo_ = False
                self.cv.notify_all()
            


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # printBar() outputs "bar". Do not change or remove this line.
            with self.cv:
                while self.foo_:
                    self.cv.wait()
                
                printBar()
                self.foo_ = True
                self.cv.notify_all()