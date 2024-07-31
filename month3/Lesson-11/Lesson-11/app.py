import schedule
import time
from datetime import datetime, timedelta

now = datetime.now()
after = datetime.now() + timedelta(minutes=1)

print(now < after)


def task():
    print("Task is running every 5 minutes.")


# Schedule the task to run every 5 minutes
schedule.every(1).minutes.do(task)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
