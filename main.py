from toaster import Toaster
import redis

INTERVAL = 1 * 100 * 60  # 1 minute


def main(redis):
    # When the file is called, Requests the user to enter.
    name = input("Enter toast name: ")
    notification_time = input("Enter toast time ex)2022 12 24 15 00: ")
    ttl = input("Enter time for the toast to stay alive: ")

    # Create an instance of the Toaster class based on the input information.
    toast = Toaster(name, notification_time, ttl, redis)
    toast.register()
    print(f"Request accepted! Toast name: {name}, Time: {notification_time}")


if __name__ == "__main__":
    redis = redis.Redis(host="localhost", port=6379, db=0)
    main(redis)
