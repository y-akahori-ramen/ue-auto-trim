# Overview
A tools for UnrealEngine that automatically trims captured video.

This tools implements the tags displayed in the upper left corner of the screen and clips the video based on the tags.

## Use Case
- Clipping a player's special skill from a captured video
- Clipping the location where the player is killed by the enemy from the captured video


## Demo
Source video.

https://user-images.githubusercontent.com/103555/233125625-2da462e4-ccc7-4699-991a-c5109564143c.mp4

One of the clipped videos.

https://user-images.githubusercontent.com/103555/233129023-53fa03ed-24f2-4305-9f50-db08587ddc01.mp4

# How to use

1. Implement trimming tag to game  
2. Play Game and Capture Video  
3. Analyze the captured video

## 1. Implement trimming tag to game
### 1-1. Add plugin to unreal engine project
Copy the [UEAutoTrim plugin folder](./Plugins/UEAutoTrim/) to the project's plugin folder.  
Then, enable the plugin in the project.

### 1-2. Implement displaying tag in game

Display the tag in the game by calling the following function through the UUEAutoTrimSystem subsystem.  

| Function | Description |
|:-|:-|
|Start|Start displaying tag.|
|End|End displaying tag.|

For Example

![](./DocResources/display_tag_example.png)

There are also functions to set the display position and color of tags. Please check [UEAutoTrimSystem.h](./Plugins/UEAutoTrim/Source/UEAutoTrim/Public/UEAutoTrimSystem.h) for details.

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
