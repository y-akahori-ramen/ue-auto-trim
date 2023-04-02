import cv2
import easyocr
import time
from enum import Enum
from moviepy.editor import *

class Mode(Enum):
    NONE = 0
    START = 1


time_sta = time.time()

video = cv2.VideoCapture('video.mp4')
print(f'frame count: {video.get(cv2.CAP_PROP_FRAME_COUNT)}')
reader = easyocr.Reader(['en'])

height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = video.get(cv2.CAP_PROP_FPS)
frame_to_secodns = 1.0 / float(fps)
print(f'height: {height}, width: {width}')
# [([[31, 65], [177, 65], [177, 81], [31, 81]],

# 最初のStart文字を見つけるまでは正確な画像位置がわからないので、画面の左上半分を対象にOCRする

default_ymax = int(height/2)
default_xmax = int(width/2)
ymax = default_ymax
xmax = default_xmax

mode = Mode.NONE

start_cound = 0
trim_name = ''
trim_info = {}

count = 0
while True:
    ret, frame = video.read()
    if ret:
        # gray scale
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # resize half size
        # gray = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)

        detframe = frame[0:ymax, 0:xmax]
        results = reader.readtext(detframe)
        for result in results:
            if mode == Mode.NONE:
                if 'AutoTrim_Start' in result[1]:
                    # ymax = result
                    print(f'StartTrim:{result[1]} Count:{count}')
                    xmax = int(result[0][1][0])
                    ymax = int(result[0][2][1])
                    mode = Mode.START
                    start_cound = count
                    trim_name = result[1]
                    # xmax = int(result[0][1][0] * 1.5)
                    # print(f'xmin: {result[0][0][0]}, xmax: {result[0][1][0]}, ymin: {result[0][0][1]}, ymax: {result[0][2][1]}')
            elif mode == Mode.START:
                if 'AutoTrim_Stop' in result[1]:
                    print(f'StopTrim:{result[1]} Count:{count}')
                    ymax = default_ymax
                    xmax = default_xmax
                    mode = Mode.NONE      
                    trim_info[trim_name] = [float(start_cound) * frame_to_secodns , float(count) * frame_to_secodns]
        count += 1
    else:
        break

for k,v in trim_info.items():
    print(f'Clip Tag:{k} Start:{v[0]}s End:{v[1]}s')
    with VideoFileClip("video.mp4",fps_source='fps').subclip(v[0]-0.5, v[1]+1) as video:
        video.write_videofile(f"video_{k}.mp4",fps=fps)
    
# print(f'count: {count}')

# video.release()

tim = time.time() - time_sta
print(tim)
