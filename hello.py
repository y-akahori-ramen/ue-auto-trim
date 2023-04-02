import cv2
import easyocr
import time


time_sta = time.time()

video = cv2.VideoCapture('video.mp4')
print(f'frame count: {video.get(cv2.CAP_PROP_FRAME_COUNT)}')
reader = easyocr.Reader(['en'])

height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
print(f'height: {height}, width: {width}')
# [([[31, 65], [177, 65], [177, 81], [31, 81]], 

# 最初のStart文字を見つけるまでは正確な画像位置がわからないので、画面の左上半分を対象にOCRする

ymax = int(height/2)
xmax = int(width/2)

count = 0
while True:
    ret, frame = video.read()
    if ret:
        count += 1

        # gray scale
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # resize half size
        # gray = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)

        detframe = frame[0:ymax,0:xmax] 
        
        results = reader.readtext(detframe)
        for result in results:
            if 'Start Recording' in result[1]:
                # ymax = result
                # print(result)
                xmax = int(result[0][1][0] * 1.5)
                ymax = int(result[0][2][1] * 1.5)
                # xmax = int(result[0][1][0] * 1.5)
                # print(f'xmin: {result[0][0][0]}, xmax: {result[0][1][0]}, ymin: {result[0][0][1]}, ymax: {result[0][2][1]}')

        print(f'count:{count}')
        # print(type(frame))
        # cv2.imshow('frame', detframe)
        # print(frame.shape)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        # if count > 2:
            # break
    else:
        break

print(f'count: {count}')

video.release()

tim = time.time()- time_sta
print(tim)
