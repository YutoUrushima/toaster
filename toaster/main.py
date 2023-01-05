from toast import Toast


def main():
    # When the file is called, Requests the user to enter.
    name = input("Enter toast name: ")
    notification_time = input("Enter toast time ex)2022 12 24 15 00: ")
    ttl = input("Enter time for the toast to stay alive: ")

    # Create an instance of the Toaster class based on the input information.
    toast = Toast(name, notification_time, ttl)
    toast.register()
    print(f"Request accepted! Toast name: {name}, Time: {notification_time}")


if __name__ == "__main__":
    main()
