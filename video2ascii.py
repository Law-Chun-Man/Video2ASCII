import cv2
import os
#import time


desired_width = 200
desired_height = 56
fps = 24
video = cv2.VideoCapture('cube.mov')

char = " ._-=+*!&#%$@"
# char = " ▁▂▃▄▅▆▇█"
length = len(char)
os.system("cls")
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))


for i in range(total_frames):
    ret, frame = video.read()

    if ret:
        resized_frame = cv2.resize(frame, (desired_width, desired_height))
        frames = ''
        for y in range(desired_height):
            for x in range(desired_width):
                b, g, r = resized_frame[y, x]
                brightness = r / 3 + g / 3 + b / 3
                index = int(brightness*length/256)
                frames += f"\033[38;2;{r};{g};{b}m{char[index]}\033[0m"
            frames += '\n'
        print("\033[H")
        print(frames)
        # time.sleep(1 / fps)
    else:
        break

video.release()
