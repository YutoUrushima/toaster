from toaster import Toaster
import datetime
from time import sleep
import schedule


def call():
    def task():
        print("hy")

    schedule.every(1).minutes.do(task)

    while True:
        schedule.run_pending()
        sleep(1)
