# ue-auto-trim
A tools for UnrealEngine that automatically trims captured video.

Tools
- UnrealEngine plugin to implement trimming tags
- Python script to trim video based on tags
# Use Case
- Clipping a player's special skill from a captured video
- Clipping the location where the player is killed by the enemy from the captured video

# How to use

1. Implement trimming tag to game  
2. Play Game and Capture Video  
3. Analyze the captured video

**Demo**
ここにデモ動画

## 1. Implement trimming tag to game
### 1-1. Add plugin to unreal engine project


### 1-2. Implement displaying tag in game

## 2. Play Game and Capture Video
Play the game and capture the video with capturing software. (eg. windows game bar)

## 3. Analyze the captured video
### 3-1. Build Docker image
```
docker buildx build -t ue-auto-trim:1.0 .
```

Reccomend to use Docker to avoid environmental problems.  
If you want to use without Docker, reference [Dockerfile](./Dockerfile) to setup environment.

### 3-2.Run
```
docker run --rm -it  --gpus=all -v {path_to_videodata_dir}:/usr/work:rw  ue-auto-trim:1.0 --video /usr/work/sample.mp4 --dist /usr/work --prefix sample_
```
| Argument | Description |
|:-|:-|
| --video | video file path |
| --dist | trim file dist path |
| --prefix | trim file prefix |
| --detect_frame_scale_x | determine the size x of the frame to be detected. 0..1 |
| --detect_frame_scale_y | determine the size y of the frame to be detected. 0..1 |
| --trim_offset_sec | offset seconds from tag to determine start and end trimming position. |

**NVIDIA Container Toolkit is required to use GPU with container**  
Check the following URL for installation.  
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker


**Use Sample Video**  
This repository contains sample video.  
You can try to trim the video with the following command.

```
cd ue-auto-trim
docker run --rm -it  --gpus=all -v $(pwd)/sampledata:/usr/work:rw ue-auto-trim:1.0 --video /usr/work/sample.mp4 --dist /usr/work --prefix sample_
```
