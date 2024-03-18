import threading

class Par_Threads:
    def _init_(self, func1, func2, params1, params2) -> None:
        self.thread1 = threading.Thread(target=func1, args=(params1))
        self.thread2 = threading.Thread(target=func2, args=(params2))

    def run(self):
        print("Thread 1 iniciada!")
        self.thread1.start()
        print("Thread 2 iniciada!")
        self.thread2.start()

        self.thread1.join()
        print("Thread 1 finalizada!")
        self.thread2.join()
        print("Thread 2 finalizada!")
    