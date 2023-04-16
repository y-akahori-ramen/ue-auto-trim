
wsl sudo service docker start
wsl docker run --rm -it  --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim/sampledata:/usr/workdata:rw  ue-auto-trim:1.0 --video /usr/workdata/sample.mp4 --dist /usr/workdata --prefix from_docker
wsl --shutdown
