import re
import redis


DATETIME_REGEXP = (
    r"\d{4}\s(0[1-9]|1[0-2])\s(0[1-9]|[12]\d|3[01])\s(0[1-9]|1\d|2[0-3])\s[0-5]\d"
)
LOCALHOST = "localhost"
PORT = 6379
DB = 0
# TODAY_REGEXP = r"today\s(0[1-9]|1\d|2[0-3])\s[0-5]\d"
# TOMORROW_REGEXP = r"tomorrow\s(0[1-9]|1\d|2[0-3])\s[0-5]\d"


class Toast:
    def __init__(self, name, message, time, ttl):
        if not re.fullmatch(DATETIME_REGEXP, time):
            raise
        self.name = name
        self.message = message
        self.time = time
        self.ttl = ttl
        self.redis = redis.Redis(host=LOCALHOST, port=PORT, db=DB)

    def register(self):
        self.redis.hset(f"Toast:{self.name}", "name", self.name)
        self.redis.hset(f"Toast:{self.name}", "message", self.message)
        self.redis.hset(f"Toast:{self.name}", "time", self.time)
        self.redis.hset(f"Toast:{self.name}", "ttl", self.ttl)
