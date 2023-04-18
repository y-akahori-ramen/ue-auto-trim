# ue-auto-trim
A tools for UnrealEngine that automatically trims captured video.

Tools
- UnrealEngine plugin to implement trimming tags
- Python script to trim video based on tags

# Demo

# Use Case
- Clipping a player's special skill from a captured video
- Clipping the location where the player is knocked down by the enemy from the captured video

# How to use
Step1. Implement trimming tag to game  
Step2. Play Game and Capture Video  
Step3. Analyze the captured video and clip the video within the range of the trimming tag

# How to display trimming tags

# How to trim video
## 1. Build Docker image
```
docker buildx build -t ue-auto-trim:1.0 .
```

Reccomend to use Docker to avoid environment problems.  
If you want to use without Docker, reference Dockerfile to setup environment.

## 2.Run
```
docker run --rm -it  --gpus=all -v {path_to_sampledata_dir}:/usr/work:rw  ue-auto-trim:1.0 --video /usr/work/sample.mp4 --dist /usr/work --prefix from_docker
```
| Argument | Description |
|:-|:-|
| --video | video file path |
| --dist | trim file dist path |
| --prefix | trim file prefix |
| --detect_frame_scale_x | determine the size x of the frame to be detected. 0..1 |
| --detect_frame_scale_y | determine the size y of the frame to be detected. 0..1 |
| --trim_offset_sec | offset seconds from tag to determine start and end trimming position. |

### To use GPU with container
NVIDIA Container Toolkit is required.

Check the following URL for installation.  
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker

