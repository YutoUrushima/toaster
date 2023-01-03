import datetime
import redis

LOCALHOST = "localhost"
PORT = 6379
DB = 0


class Toaster:
    def __init__(self):
        self.redis = redis.Redis(host=LOCALHOST, port=PORT, db=DB)

    def fetch(self, key):
        fetched_info = {}
        fetched_info.setdefault("name", self.redis.hget(key, "name"))
        fetched_info.setdefault("ttl", self.redis.hget(key, "ttl"))
        return fetched_info

    def search(self):
        current_time = datetime.datetime.now()
        corresponding_toastors = []
        all_keys = (
            self.redis.keys()
        )  # DOCS says "Don't use KEYS in your regular application code." However, the number of records is not large and this is not a command that is struck in parallel.
        for key in all_keys:
            decoded_key = key.decode("utf-8")
            if self.redis.type(decoded_key).decode("utf-8") != "hash":
                continue
            toast_time = self.redis.hget(decoded_key, "time").decode("utf-8").split(" ")
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

    def delete(self, key):
        self.redis.delete(key)
        print(f"Toast deleted: {key}")
