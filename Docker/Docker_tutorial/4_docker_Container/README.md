# 容器(Container)

### 新建並啟動容器(Container)

主要command為 docker run

`docker run -t -i -d <IMAGE_ID>`

`docker run -t -i -d <CONTAINER_Name>:<Tag>`

```bash
$ sudo docker run ubuntu:14.04 /bin/echo 'Hello world'
Hello world
```

以下的命令則啟動一個 bash 終端，允許使用者進行互動。

```bash
$ sudo docker run -t -i ubuntu:14.04 /bin/bash
root@74fe38d11401 :/#
```
參數:<br />
 -t: 讓Docker分配一個虛擬終端（pseudo-tty) <br />
 -i: 互動模式,讓容器的標準輸入保持打開<br />
 -d: 背景執行<br />
 > -t: --tty <br />
 -i: --interactive <br />
 -d: --detach

### 關閉容器(Container)
查看目前 Image


```bash
~$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
ubuntu        14.04     13b66b487594   2 weeks ago     197MB
~$ docker run -t -i -d 13b66b487594 #在背景啟動 command
~$ docker run -t -i -d ubuntu:14.04 #在背景啟動 command
```
查看目前已啟動的容器(Container)

```bash
~$ docker ps
CONTAINER ID   IMAGE          COMMAND       CREATED         STATUS         PORTS     NAMES
6f64bb234e90   13b66b487594   "/bin/bash"   3 seconds ago   Up 2 seconds             boring_gould

```
關閉容器

`docker stop <CONTAINER_ID>`

`docker stop <Image>`

```bash
~$ docker stop 6f64bb234e90
6f64bb234e90
~$ docker ps #在確認一次，是否關閉
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```


