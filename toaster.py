from plyer import notification


class Toaster:
    def __init__(self, name, time, ttl):
        self.name = name
        self.time = time
        self.ttl = ttl

    def register(self):
        # register to MongoDB
        print("registerd!")

    def call(self):
        notification.notify(title="toaster", message=self.name, timeout=self.ttl)
