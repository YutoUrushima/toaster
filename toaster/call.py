from toaster import Toaster
import datetime
from time import sleep
import schedule


def call():
    print("hy")


schedule.every(1).minutes.do(call)

while True:
    schedule.run_pending()
    sleep(1)
