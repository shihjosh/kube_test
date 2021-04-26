# 倉庫（Repository）

倉庫（Repository）是存放映像檔的地方。

### Docker Hub

[前往註冊Docker Hub的帳號](https://hub.docker.com/ "前往註冊Docker Hub的帳號")

Docker 官方提供了一個公共倉庫 Docker Hub，都可以透過在 Docker Hub 中直接下載映像檔來使用。

### 基本操作

搜尋 Docker image

`docker search <IMAGE_NAME>`

下載 Docker Image

`docker pull <IMAGE_NAME>:<Tag>`

搜尋 Docker image
```bash
$ docker search ubuntu
NAME                                                      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
ubuntu                                                    Ubuntu is a Debian-based Linux operating sys…   12133     [OK]       
dorowu/ubuntu-desktop-lxde-vnc                            Docker image to provide HTML5 VNC interface …   523                  [OK]
websphere-liberty                                         WebSphere Liberty multi-architecture images …   267       [OK]       
rastasheep/ubuntu-sshd                                    Dockerized SSH service, built on top of offi…   249                  [OK]
consol/ubuntu-xfce-vnc                                    Ubuntu container with "headless" VNC session…   236                  [OK]

```

下載 Docker Image
```bash
$ docker pull docker pull ubuntu:latest
```