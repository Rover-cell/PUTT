import keyboard
from PIL import ImageGrab, Image
import pytesseract
import pygame
import os

#Change directory as needed
base_dir = r"C:\Users\User\Project\ObjectDetectionProject\ComputerVisionTasks\Object-detection"

pygame.init()
pygame.mixer.init()

screenshot = ImageGrab.grab()

print("Taking a screenshot...")
screenshot.save("picturetaken.png", "PNG")
    
print("Converting picture to string...")
picture = pytesseract.image_to_string(Image.open('picturetaken.png'))
