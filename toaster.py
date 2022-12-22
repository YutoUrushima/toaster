from plyer import notification
import redis


class Toaster:
    def __init__(self, name, time, ttl):
        self.name = name
        self.time = time
        self.ttl = ttl
        self.redis = redis.Redis(host="localhost", post=6379, db=0)

    def register(self):
        self.redis.set(self.name, self.time)

    def call(self):
        notification.notify(title="toaster", message=self.name, timeout=self.ttl)
