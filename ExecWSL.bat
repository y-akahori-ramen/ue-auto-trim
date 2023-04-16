
wsl sudo service docker start
wsl docker run --rm -it --gpus=all -v /mnt/c/MyPrograms/ue-auto-trim:/usr/trim:rw  -w /usr/trim  ue-auto-trim-pure:1.0 python3 hello.py  
wsl --shutdown
