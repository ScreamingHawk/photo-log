#! /usr/bin/env python3

from pygame import camera, image
from os import listdir, path
import schedule
import time
import re

IMG_FOLDER = "imgs"

def init_camera():
    """Initialise the camera"""
    camera.init()
    camlist = camera.list_cameras()
    if not camlist:
        print("No cameras detected!")
        exit(1)
    return camera.Camera(camlist[0])

def request_schedule():
    """Requests and creates the schedule which to run the capture"""
    freq = input("What frequency for capturing? (once/1sec/1min/1hour/1day)")
    num = int(re.search(r'\d+', freq)[0])
    period = re.search(r'[^\d\W]+', freq)[0]
    sched = schedule.every(num)
    if period == "sec":
        sched = sched.seconds
    elif period == "min":
        sched = sched.minutes
    elif period == "hour":
        sched = sched.hours
    elif period == "day":
        sched = sched.days
    elif period == "once":
        print("Running once")
        return None
    else:
        print("Schedule not detected!")
        exit(2)
    print(f'Running every {num} {period}s')
    return sched

def capture_image(cam):
    """Capture an image from the camera and save it to disk"""
    # Get image filename by counting items in folder
    img_count = len([name for name in listdir(IMG_FOLDER) if path.isfile(path.join(IMG_FOLDER, name))])
    img_name = f'image{img_count:06}.jpg'
    # Save image
    cam.start()
    img = cam.get_image()
    print(f'Saving {img_name}')
    image.save(img, path.join(IMG_FOLDER, img_name))
    cam.stop()

if __name__ == "__main__":
    cam = init_camera()
    sched = request_schedule()
    # Run immediately then schedule
    capture_image(cam)
    if (sched):
        sched.do(capture_image, cam=cam)

    while True:
        schedule.run_pending()
        time.sleep(1)
