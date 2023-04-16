import cv2
import easyocr
from enum import Enum
from moviepy.editor import VideoFileClip
import time
import os
import argparse


class Mode(Enum):
    DETECT_TRIM_START = 0
    DETECT_TRIM_END = 1


def trim(video_file: str,  trimfile_dist: str, trimfile_prefix: str, detect_frame_scale_x: float = 0.5, detect_frame_scale_y: float = 0.5, trim_offset_sec: float = 1.0):
    video = cv2.VideoCapture(video_file)
    reader = easyocr.Reader(['en'])

    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_to_secodns = 1.0 / float(fps)

    default_detect_xmax = int(float(width)*detect_frame_scale_x)
    default_detect_ymax = int(float(height)*detect_frame_scale_y)

    detect_xmax = default_detect_xmax
    detect_ymax = default_detect_ymax

    mode = Mode.DETECT_TRIM_START

    start_cound = 0
    trim_name = ''
    trim_info = {}

    count = 0

    print('Analyzing...')
    while True:
        ret, frame = video.read()
        if ret:
            detframe = frame[0:detect_ymax, 0:detect_xmax]
            results = reader.readtext(detframe)
            for result in results:
                if mode == Mode.DETECT_TRIM_START:
                    if 'AutoTrim_Start' in result[1]:
                        detect_xmax = int(result[0][1][0])
                        detect_ymax = int(result[0][2][1])
                        mode = Mode.DETECT_TRIM_END
                        start_cound = count
                        trim_name = result[1]
                        print(f'Trim start detected Tag:{trim_name} FrameCount:{count} Sec:{float(start_cound) * frame_to_secodns}')
                elif mode == Mode.DETECT_TRIM_END:
                    if 'AutoTrim_End' in result[1]:
                        detect_ymax = default_detect_ymax
                        detect_xmax = default_detect_xmax
                        mode = Mode.DETECT_TRIM_START
                        trim_info[trim_name] = [float(start_cound) * frame_to_secodns, float(count) * frame_to_secodns]
                        print(f'Trim end detected Tag:{trim_name} FrameCount:{count} Sec:{float(count) * frame_to_secodns}')
            count += 1
        else:
            break

    print('Cliping...')
    for k, v in trim_info.items():
        with VideoFileClip(video_file, fps_source='fps').subclip(v[0]-trim_offset_sec, v[1]+trim_offset_sec) as video:
            video.write_videofile(os.path.join(trimfile_dist, f'{trimfile_prefix}_{k}.mp4'), fps=fps)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', type=str, required=True)
    parser.add_argument('--dist', type=str, required=True)
    parser.add_argument('--prefix', type=str, required=True)
    parser.add_argument('--detect_frame_scale_x', type=float, default=0.5)
    parser.add_argument('--detect_frame_scale_y', type=float, default=0.5)
    parser.add_argument('--trim_offset_sec', type=float, default=1.0)

    args = parser.parse_args()
    start = time.time()
    trim(args.video, args.dist, args.prefix, args.detect_frame_scale_x, args.detect_frame_scale_y, args.trim_offset_sec)
    print(f'time:{time.time()-start}')
