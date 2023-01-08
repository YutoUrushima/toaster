import re
import redis
import json
import sys


DATETIME_REGEXP = (
    r"\d{4}\s(0[1-9]|1[0-2])\s(0[1-9]|[12]\d|3[01])\s(0[1-9]|1\d|2[0-3])\s[0-5]\d"
)
TTL_REGEXP = r"\d?\d"


class Toast:
    def __init__(self, name, message, time, ttl):
        if not name:
            print("Please enter some characters as a name.")
            sys.exit()
        if not re.fullmatch(DATETIME_REGEXP, time):
            print(
                "Date and time format is incorrect. Please enter as in the example. ex) January 1, 2023 at 21:00 => 2023 01 01 21 00"
            )
            sys.exit()
        if not re.fullmatch(TTL_REGEXP, ttl):
            print(
                "The time for the toast to stay alive format is incorrect, please enter 0 ~ 99."
            )
            sys.exit()

        json_file = open("./setting.json", "r")
        redis_setting = json.load(json_file)

        self.name = name
        self.message = message
        self.time = time
        self.ttl = ttl
        self.redis = redis.Redis(
            host=redis_setting["redis"]["localhost"],
            port=redis_setting["redis"]["port"],
            db=redis_setting["redis"]["db"],
        )

    def register(self):
        self.redis.hset(f"Toast:{self.name}", "name", self.name)
        self.redis.hset(f"Toast:{self.name}", "message", self.message)
        self.redis.hset(f"Toast:{self.name}", "time", self.time)
        self.redis.hset(f"Toast:{self.name}", "ttl", self.ttl)
