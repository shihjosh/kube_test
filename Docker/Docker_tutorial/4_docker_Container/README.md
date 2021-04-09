# 容器(Container)

### 新建並啟動容器(Container)

主要commamd為 docker run

```bash
$ sudo docker run ubuntu:14.04 /bin/echo 'Hello world'
Hello world
```

以下的命令則啟動一個 bash 終端，允許使用者進行互動。

```bash
$ sudo docker run -t -i ubuntu:14.04 /bin/bash
root@74fe38d11401 :/#
```
參數:
 -t:(--tty) 讓Docker分配一個虛擬終端（pseudo-tty) 
 -i:(--interactive) 互動模式,讓容器的標準輸入保持打開。
 -d:(--detach) 背景執行
 > -t: --tty <br />
 -i: --interactive <br />
 -d: --detach

