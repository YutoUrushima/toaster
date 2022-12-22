from plyer import notification


class Toaster:
    def __init__(self, name, time, ttl, redis):
        self.name = name
        self.time = time
        self.ttl = ttl
        self.redis = redis

    def register(self):
        self.redis.set(self.name, self.time)

    def fetch(self, name):
        return self.redis.get(name)

    def call(self):
        notification.notify(title="toaster", message=self.name, timeout=self.ttl)
