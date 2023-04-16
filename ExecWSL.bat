
wsl sudo service docker start
wsl docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim/data:/usr/workdata:rw  ue-auto-trim:1.0 --video /usr/workdata/video3.mp4 --dist /usr/workdata --prefix from_docker
wsl --shutdown
