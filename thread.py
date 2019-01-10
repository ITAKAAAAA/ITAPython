import threading

class MaxMessanger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = MaxMessanger(name="Send out messages")
y = MaxMessanger(name="Receive messages")
x.start()
y.start()