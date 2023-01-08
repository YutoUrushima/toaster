import datetime
import redis
import json
import sys


class Toaster:
    def __init__(self):
        json_file = open("./setting.json", "r")
        redis_setting = json.load(json_file)

        self.redis = redis.Redis(
            host=redis_setting["redis"]["localhost"],
            port=redis_setting["redis"]["port"],
            db=redis_setting["redis"]["db"],
        )

    def fetch(self, key):
        try:
            fetched_info = {}
            fetched_info.setdefault("name", self.redis.hget(key, "name"))
            fetched_info.setdefault("message", self.redis.hget(key, "message"))
            fetched_info.setdefault("ttl", self.redis.hget(key, "ttl"))
            return fetched_info
        except redis.exceptions.ConnectionError:
            print("ERROR: Cannot connect to Redis. Please check your settings.")
            sys.exit()

    def search(self):
        try:
            current_time = datetime.datetime.now().replace(second=0, microsecond=0)
            corresponding_toastors = []
            all_keys = (
                self.redis.keys()
            )  # DOCS says "Don't use KEYS in your regular application code." However, the number of records is not large and this is not a command that is struck in parallel.
            for key in all_keys:
                decoded_key = key.decode("utf-8")
                if self.redis.type(decoded_key).decode("utf-8") != "hash":
                    continue
                toast_time = (
                    self.redis.hget(decoded_key, "time").decode("utf-8").split(" ")
                )
                encoded_toast_time = datetime.datetime(
                    int(toast_time[0]),  # Year
                    int(toast_time[1]),  # Month
                    int(toast_time[2]),  # Day
                    int(toast_time[3]),  # Hour
                    int(toast_time[4]),  # Minute
                )
                if encoded_toast_time == current_time:
                    corresponding_toastors.append(decoded_key)
            return corresponding_toastors
        except redis.exceptions.ConnectionError:
            print("ERROR: Cannot connect to Redis. Please check your settings.")
            sys.exit()
        except ValueError:
            print(
                "ERROR: An unexpected error has occurred. Perhaps an unexpected value was entered into a record of type Hash in Redis."
            )
            sys.exit()

    def delete(self, key):
        try:
            self.redis.delete(key)
            print(f"Toast deleted: {key}")
        except redis.exceptions.ConnectionError:
            print("ERROR: Cannot connect to Redis. Please check your settings.")
            sys.exit()
