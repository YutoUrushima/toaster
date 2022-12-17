import toaster
import time
import datetime

INTERVAL = 1 * 100 * 60 # 1 minute

def main():
  # When the file is called, Requests the user to enter.
  name = input("Enter toast name: ")
  notification_time = input("Enter toast time: ")
  ttl = input("Enter time for the toast to stay alive: ")

  # Create an instance of the Toaster class based on the input information.
  toast = toaster.Toaster(name, notification_time, ttl)
  print(f'Request accepted! Toast name: {toast.name}, Time: {toast.time}')

  # Every minute, check the current time and execute a toast notification if it is the same as the set time.
  while(True):
    if datetime.datetime() == toast.time:
      toast.call()
      break
    else:
      time.sleep(INTERVAL)

if __name__ == "__main__":
  main()