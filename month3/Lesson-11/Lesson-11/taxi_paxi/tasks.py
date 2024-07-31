import time

import schedule
from announcement import check_ann_is_active

schedule.every(1).minutes.do(check_ann_is_active)
while True:
    schedule.run_pending()
    time.sleep(1)