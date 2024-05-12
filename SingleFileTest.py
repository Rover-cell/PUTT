import cv2
import matplotlib.pyplot as plt
import keyboard
from PIL import ImageGrab, Image
import pytesseract
import pygame
import os
import time

print("Current working directory:", os.getcwd())
base_dir = r"C:\Users\User\Project\ObjectDetectionProject\ComputerVisionTasks\Object-detection"

pygame.init()
pygame.mixer.init()

# File names
class_file = "coco.names"
config_file = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weights_file = "frozen_inference_graph.pb"
audio = 'oof.mp3'

def takeScreenshot():
    screenshot = ImageGrab.grab()

    print("Taking a screenshot...")
    screenshot.save("picturetaken.png", "PNG")

# Absolute paths to files
classFile = os.path.join(base_dir, class_file)
configPath = os.path.join(base_dir, config_file)
weightsPath = os.path.join(base_dir, weights_file)
audioPath = os.path.join(base_dir, audio)

# Check if files exist
if not os.path.isfile(classFile):
    print("Class file not found at:", classFile)
    exit()

if not os.path.isfile(configPath):
    print("Config file not found at:", configPath)
    exit()

if not os.path.isfile(weightsPath):
    print("Weights file not found at:", weightsPath)
    exit()

# Load the model
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Load the image
def doObjectDetection():
    #Searches for the screenshot file
    img = cv2.imread(os.path.join(base_dir, 'picturetaken.png'))
    if img is None:
        print("Error: Failed to load image from", base_dir)
        exit()

    # Detect objects in the screenshot image
    print("Detecting objects...")
    classIds, confs, bbox = net.detect(img, confThreshold=0.5)

    # Draw bounding boxes
    if len(classIds) > 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(img, box, color=(255, 0, 0), thickness=3)
            cv2.putText(img, str(classId), (box[0] + 5, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(img, str(round(confidence * 100, 2)), (box[0] + 5, box[1] + 55), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)

    # Display the image with detected objects
    print("Displaying image with detected objects...")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for matplotlib
    plt.show()

def main():
    print("Press the Escape key (Esc) to exit.")
    print("Current working directory:", os.getcwd())

    while True:

        takeScreenshot()
        doObjectDetection()

        screenshot2 = ImageGrab.grab()

        plt.show(block=False)
        plt.pause(3)
        plt.close('all')

        print("Taking a screenshot...")
        screenshot2.save("picture.png", "PNG")

        # Converts the 2nd screenshot into a string
        print("Converting picture to string...")
        picture = pytesseract.image_to_string(Image.open(os.path.join(base_dir, 'picture.png')))

        # Checks for the number 1 in the 2nd screenshot
        if "1" in picture.lower():
            pygame.mixer.music.load(audioPath)
            print("Playing audio...")
            pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)



if __name__ == "__main__":
    main()
