import os
import subprocess
import sys
import keyboard

"""  
What this program SHOULD do:
1. Take a screenshot of the screen
2. Perform object detection on the screenshot
3. Display the image with detected objects in it
4. Take a screenshot of the window display before closing the window
5. Convert the screenshot into a text
6. Checks if the desired word, in this case is "yes", is in the text
7. If the word is in the text, play an audio
8. If it doesn't find the word, loops back to Step 1 and does the whole thing again

What this program DOESN'T do:
Everything starting from Step 4.
"""

def main():

    while True:
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Step 1: Take screenshot
        subprocess.run(["python", os.path.join(current_dir, "TakeScreenshot.py")])

        # Step 2: Run object detection on the screenshot and display it
        subprocess.run(["python", os.path.join(current_dir, "ObjectDetection.py")])

        #Step 3: Takes a screenshot and closes the window AUTOMATICALLY but it doesn't fucking work
        #        and I don't know why
        subprocess.run(["python", os.path.join(current_dir, "Screenshot2.py")])

if __name__ == "__main__":
    main()
