from toaster import Toaster
from time import sleep
import schedule
from plyer import notification
import sys


def call():
    try:
        toasts_list = toaster.search()
        if len(toasts_list) < 1:
            return
        for toast in toasts_list:
            toast_dict = toaster.fetch(toast)
            notification.notify(
                title=toast_dict["name"].decode("utf-8"),
                message=toast_dict["message"].decode("utf-8"),
                timeout=int(toast_dict["ttl"].decode("utf-8")),
            )
            print(f'Toast called: {toast_dict["name"]}')
            toaster.delete(toast)
    except ValueError:
        print(
            "ERROR: An unexpected error has occurred. Perhaps an unexpected value was entered into a record of type Hash in Redis."
        )
        sys.exit()


schedule.every().minute.at(":00").do(call)

if __name__ == "__main__":
    toaster = Toaster()

    while True:
        schedule.run_pending()
        sleep(1)
