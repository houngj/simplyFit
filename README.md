# simply_fit
Simple daily fitness tracker

README in progress

Waffle.io URL: https://waffle.io/houngj/simply_fit

Running simply_fit
1) Install Docker, reference https://docs.docker.com/docker-for-mac/install/
2) Clone simply_fit
3) Run "docker build -t yourname/simply_fit /location/of/cloned/repo/"
4) Run "docker run --name=simply_fit \
    --detach=true \
    --restart=always \
    --publish=8001:8000 \
    yourname/simply_fit:latest"
5) Access localhost:8001 from favorite browser
