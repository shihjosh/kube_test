# 映像檔(Images)

### 抓取映像檔

docker pull 命令從倉庫(docker hub)取得所需要的映像檔。

```bash
$ sudo docker pull ubuntu:20.04
```
下載完成後，就可以使用該映像檔了

例如:建立一個容器。

### 列出-映像檔

docker images 顯示本機已有的映像檔。

```bash
$ sudo docker images
```
會列印出一些訊息(有空再補充)

### 移除-映像檔(Images)

要移除映像檔，可以使用 docker rmi 命令。
注意 docker rm 命令是移除容器。


```bash
$ sudo docker rmi <images_name>
$ sudo docker rmi -f <image_ID>

$ sudo docker images // 顯示一下目前所有的 image 
REPOSITORY       TAG      IMAGE ID      CREATED      VIRTUAL SIZE
ubuntu           12.04    74fe38d11401  4 weeks ago  209.6 MB

ex:
$ sudo docker rmi ubuntu:20.04    // 使用 image name 刪除
$ sudo docker rmi -f 74fe38d11401 // 使用 image ID 並強制刪除
```
參數:
  -f : 強制刪除的意思
