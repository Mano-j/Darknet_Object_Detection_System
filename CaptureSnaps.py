from cv2 import *
import time


def snapPic(imageNumber):
    s, img = cam.read()

    if s:  # frame captured without any errors
        imwrite(str(imageNumber) + ".Capture.jpg", img)  # save image


# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
imageNumber = 1
number_of_images = 10  # number of recent images to be saved
timeInterval = 1       # seconds

choice = int(input("Do you want to save all your captured images (1) or just the recent (2) \nEnter your choice: "))
onlyRecent = None
if choice == 1:
    onlyRecent = False
elif choice == 2:
    onlyRecent = True
else:
    print("Please enter a valid choice.")
    exit(-1)

while True:
    if onlyRecent and imageNumber > number_of_images:
        imageNumber = 1

    snapPic(imageNumber)
    time.sleep(timeInterval)
    imageNumber += 1
