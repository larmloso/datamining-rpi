# import time
# from picamera import PiCamera
# 
# cam = PiCamera()
# cam.start_preview()
# time.sleep(5)
# 
# cam.capture('image91.jpg')

from datetime import datetime

today = datetime.now().strftime("%d%m%Y-%H-%M-%S")

print(today)