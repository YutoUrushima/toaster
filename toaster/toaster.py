from plyer import notification
import re
import datetime
import redis

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
    def search(cls):
        current_time = datetime.datetime.now()
        corresponding_toastors = []
        all_keys = cls.redis.keys()
        for key in all_keys:
            decoded_key = key.decode("utf-8")
            if cls.redis.type(decoded_key).decode("utf-8") != "hash":
                continue
            toast_time = cls.redis.hget(decoded_key, "time").decode("utf-8").split(" ")
            encoded_toast_time = datetime.datetime(
                int(toast_time[0]),
                int(toast_time[1]),
                int(toast_time[2]),
                int(toast_time[3]),
                int(toast_time[4]),
            )
            if encoded_toast_time == current_time:
                corresponding_toastors.append(decoded_key)
        return corresponding_toastors

    @classmethod
    def call(self):
        notification.notify(title="toaster", message=self.name, timeout=self.ttl)
