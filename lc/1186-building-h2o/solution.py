from threading import Semaphore, Barrier 

class H2O:
    def __init__(self):
        self.semp_h = Semaphore(2)
        self.semp_o = Semaphore(1)
        self.barrier = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        with self.semp_h:
            self.barrier.wait()
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        with self.semp_o:
            self.barrier.wait()
            releaseOxygen()
