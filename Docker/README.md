# 安裝 Docker

```bash
#系統更新
$ sudo apt update
$ sudo apt upgrade
$ sudo apt autoremove
```

```bash
#安裝系統依賴包
$ sudo apt-get install\
 apt-transport-https\
 ca-certificates\
 curl\
 gnupg-agent\
 software-properties-common
```

```bash
#加入 Docker 訊息密鑰
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg |sudo apt-key add -
9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88
```

```bash
#確認密鑰
$ apt-key list
#最後8為做為fingerprint參數
$ sudo apt-key fingerprint 0EBFCD88
```

```bash
#將Docker訊息庫加入本地訊息庫
#設定repository
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

```bash
#查看OS採用核心
$ lsb_release -cs
#查看訊息庫加入的位置內容
$ cat /etc/apt/sources.list|grep docker
```

```bash
#系統在更新
$ sudo apt update
$ sudo apt upgrade
```

```bash
#Docker 安裝
$ apt show docker-ce
$ sudo apt install docker-ce docker-ce-cli containerd.io
#安裝驗證
$ docker help
$ docker version
$ sudo docker run hello-world
```

我們可以把目前使用者加到docker群組裡面, 當docker service 起來時, 會以這個群組的成員來初始化相關服務

```python
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
```

以下是成功畫面----有空再補


Malformed entry 52 in list file /etc/apt/sources.list (URI parse)

```jsx
his message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```
