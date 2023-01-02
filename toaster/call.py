from toaster import Toaster
import datetime
from time import sleep
import schedule


# def call():
#     print("hy")


# schedule.every(1).minutes.do(call)

# while True:
#     schedule.run_pending()
#     sleep(1)


def ex_search():
    array = Toaster.search()
    print(array)


ex_search()
