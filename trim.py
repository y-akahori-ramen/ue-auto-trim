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


def trim(
        video_file: str,  trimfile_dist: str, trimfile_prefix: str,
        detect_frame_scale_x: float, detect_frame_scale_y: float,
        trim_offset_sec: float):
    """Trim video file by AutoTrim_Start and AutoTrim_End tag
    """
    video = cv2.VideoCapture(video_file)
    reader = easyocr.Reader(['en'])

    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    fps = video.get(cv2.CAP_PROP_FPS)
    total_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
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
                        trim_name = trim_name.replace('AutoTrim_Start', '')
                        if trim_name in trim_info:
                            trim_name = f'{trim_name}_{count}'
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
        t_start = max(v[0]-trim_offset_sec, 0)
        t_end = min(v[1]+trim_offset_sec, total_frame*frame_to_secodns)
        with VideoFileClip(video_file, fps_source='fps').subclip(t_start, t_end) as video:
            video.write_videofile(os.path.join(trimfile_dist, f'{trimfile_prefix}_{k}.mp4'), fps=fps)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Trim video file by AutoTrim_Start and AutoTrim_End tag')
    parser.add_argument('--video', type=str, required=True, help='video file path')
    parser.add_argument('--dist', type=str, required=True, help='trim file dist path')
    parser.add_argument('--prefix', type=str, required=True, help='trim file prefix')
    parser.add_argument('--detect_frame_scale_x', type=float, default=0.5, help='determine the size x of the frame to be detected. 0..1')
    parser.add_argument('--detect_frame_scale_y', type=float, default=0.5, help='determine the size y of the frame to be detected. 0..1')
    parser.add_argument('--trim_offset_sec', type=float, default=1.0,  help='offset seconds from tag to determine start and end trimming position.')

    args = parser.parse_args()
    start = time.time()
    trim(args.video, args.dist, args.prefix, args.detect_frame_scale_x, args.detect_frame_scale_y, args.trim_offset_sec)
    print(f'time:{time.time()-start}')
