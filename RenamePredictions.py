import os
import time


path = os.getcwd()
#       OR
# path = "replace_with_path_to_dir"

predictionNumber = 0
timeInterval = 4  # seconds
onlyRecent = True

while True:
    for file in os.listdir(path):
        fileName, fileExt = os.path.splitext(file)
        # print(fileName)
        if fileName.startswith("predictions"):
            predictionNumber += 1

            if onlyRecent and predictionNumber > 10:
                predictionNumber = 1

            fileName = str(predictionNumber) + "." + fileName
            try:
                os.rename(file, "{}{}".format(fileName, fileExt))

            # if file already present with same name - overwrite
            except WindowsError:
                os.remove("{}{}".format(fileName, fileExt))
                os.rename(file, "{}{}".format(fileName, fileExt))

    # Adjust the time interval at which the program scans through the files again
    # according to your system performance(how long on average it takes to make a prediction using Darknet)
    time.sleep(timeInterval)
