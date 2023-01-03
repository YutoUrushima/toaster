from toaster import Toaster
from time import sleep
import schedule
from plyer import notification

toaster = Toaster()


def call():
    toasts_list = toaster.search()
    if len(toasts_list) < 1:
        return
    for toast in toasts_list:
        toast_dict = toaster.fetch(toast)
        notification.notify(
            title="toaster", message=toast_dict["name"], timeout=toast_dict["ttl"]
        )
        print(f'Toast called: {toast_dict["name"]}')
        toaster.delete(toast)


schedule.every().minute.at(":00").do(call)

while True:
    schedule.run_pending()
    sleep(1)
