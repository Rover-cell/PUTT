import keyboard
from PIL import ImageGrab, Image
import pytesseract
import pygame
import os
import cv2
import matplotlib.pyplot as plt

base_dir = r"C:\Users\User\Project\ObjectDetectionProject\ComputerVisionTasks\Object-detection"

pygame.init()
pygame.mixer.init()

screenshot = ImageGrab.grab()
audio = os.path.join(base_dir, 'oof.mp3')

print("Taking a screenshot...")
screenshot.save("picturetaken.png", "PNG")

plt.close()

print("Converting picture to string...")
picture = pytesseract.image_to_string(Image.open('picturetaken2.png'))

if "yes" in picture.lower():
        pygame.mixer.music.load(audio)
        print("Playing audio...")
        pygame.mixer.music.play()
        
while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

