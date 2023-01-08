from toast import Toast


def main():
    # Input toast time
    name = input("Enter toast name: ")
    message = input("Enter additional messages If you have them: ")
    notification_time = input(
        "Enter toast time in the format 'yyyy mm dd HH mm': "
    )  # ex)2022 12 24 15 00
    ttl = input("Enter time for the toast to stay alive: ")

    # Record the toast
    toast = Toast(name, message, notification_time, ttl)
    toast.register()
    print(
        f"Request accepted! Toast name: {name}, messgae: {message}, Time: {notification_time}"
    )


if __name__ == "__main__":
    main()
