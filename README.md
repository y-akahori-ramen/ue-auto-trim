# ue-auto-trim
A tool for UnrealEngine that automatically trims captured video.

- UnrealEngine plug-in to display trimming tags
- A tool that analyzes the video trimming tags and splits the video within the range of the tags

# How it works
Step1. Implemented trimming tag to game
Step2. Play Game and Capture Video
Step3. Analyze the captured video and clip the video within the range of the trimming tag

# Use Case
- Clipping a player's special skill from a captured video
- Clipping the location where the player is knocked down by the enemy from the captured video

# How to display trimming tags

# How to trim video
## 1. Build Docker image
```
docker buildx build -t ue-auto-trim:1.0 .
```

## 2.Run
```
docker run --rm -it  --gpus=all -v {path_to_sampledata_dir}:/usr/work:rw  ue-auto-trim:1.0 --video /usr/work/sample.mp4 --dist /usr/work --prefix from_docker
```

NVIDIA Container Toolkit is required to use GPU with container.
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker




# torchvision torchaudio

python 3.9.13
CUDA 11.8

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

いまだとgitのリポジトリを直接installしないとエラーがでる
pip3 install git+https://github.com/JaidedAI/EasyOCR.git


pip3 install moviepy


apt update
apt upgrade


C:\MyPrograms\ue-auto-trim\video3.mp4

 libbz2-dev
docker run --rm -it  --gpus=all -v C:\MyPrograms\ue-auto-trim\:/usr/trim:rw ue-auto-trim:1.0 


最初に言語データのinstallが入るので、そこだけはdockerfile内でやっておくとよい

こんてなで実行した場合     111秒
windowsから実行した場合  142秒
おそらく、誤差だろう

docker run --rm -it  --gpus=all -v C:\MyPrograms\ue-auto-trim\:/usr/trim:rw ue-auto-trim-pure:1.0


docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim:/usr/trim:rw -w /usr/trim ue-auto-trim:1.0
docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim:/usr/trim:rw ue-auto-trim:1.0
docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim:/usr/trim:rw ue-auto-trim-pure:1.0

docker desktopを使っているとNVIDIAのイメージから作らなくてもGPU使ってくれる


docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim:/usr/trim:rw  -w /usr/trim  ue-auto-trim-pure:1.0 python3 hello.py  


docker buildx build -t ue-auto-trim:1.0 .

docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim:/usr/trim:rw  -w /usr/trim  ue-auto-trim:1.0 python3 hello.py  



docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim/data:/usr/workdata:rw  ue-auto-trim:1.0 --video /usr/workdata/video3.mp4 --dist /usr/workdata --prefix from_docker

docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim:/usr/trim:rw  ue-auto-trim:1.0 

docker run --rm -it  -v /Volumes/Data/programs/ue-auto-trim/sampledata:/usr/workdata:rw  ue-auto-trim:1.0 --video /usr/workdata/sample.mp4 --dist /usr/workdata --prefix from_docker
docker run --rm -it  --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim/sampledata:/usr/workdata:rw  ue-auto-trim:1.0 --video /usr/workdata/sample.mp4 --dist /usr/workdata --prefix from_docker
