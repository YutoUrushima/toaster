from plyer import notification
import re

DATETIME_REGEXP = (
    r"\d{4}\s(0[1-9]|1[0-2])\s(0[1-9]|[12]\d|3[01])\s(0[1-9]|1\d|2[0-3])\s[0-5]\d"
)
# TODAY_REGEXP = r"today\s(0[1-9]|1\d|2[0-3])\s[0-5]\d"
# TOMORROW_REGEXP = r"tomorrow\s(0[1-9]|1\d|2[0-3])\s[0-5]\d"


class Toaster:
    redis = None

    def __init__(self, name, time, ttl, redis):
        if not re.fullmatch(DATETIME_REGEXP, time):
            raise
        self.name = name
        self.time = time
        self.ttl = ttl
        Toaster.redis = self.redis = redis

    def register(self):
        self.redis.hset(f"Toast:{self.name}", "name", self.name)
        self.redis.hset(f"Toast:{self.name}", "time", self.time)
        self.redis.hset(f"Toast:{self.name}", "ttl", self.ttl)

    @classmethod
    def fetch(cls, name, key):
        return cls.redis.hget(f"Toast:{name}", key)

    @classmethod
    def search(cls, now):
        corresponding_toastors = []
        all_keys = cls.redis.keys
        for key in all_keys:
            time = cls.redis.hget(key, "time")
            if time == now:
                corresponding_toastors.append(key)
        return corresponding_toastors

    @classmethod
    def call(self):
        notification.notify(title="toaster", message=self.name, timeout=self.ttl)
