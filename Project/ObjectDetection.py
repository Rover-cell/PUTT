import os
import cv2
import matplotlib.pyplot as plt
import subprocess
import time

#For debugging purposes
print("Current working directory:", os.getcwd())
base_dir = r"C:\Users\User\Project\ObjectDetectionProject\ComputerVisionTasks\Object-detection"
current_dir = os.path.dirname(os.path.abspath(__file__))

# File names
class_file = "coco.names"
config_file = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weights_file = "frozen_inference_graph.pb"

# Absolute paths to files
classFile = os.path.join(base_dir, class_file)
configPath = os.path.join(base_dir, config_file)
weightsPath = os.path.join(base_dir, weights_file)

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

# Image path
image_path = os.path.join(base_dir, "picturetaken.png")

# Load the image
img = cv2.imread(image_path)
if img is None:
    print("Error: Failed to load image from", image_path)
    exit()

# Detect objects in the image
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