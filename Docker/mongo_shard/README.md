## K8s MongoDB Shard 安裝

kubernetes: v1.18.5
image: mongo:4.4.2

####1.Create Namespace
```Bash
$ kubectl apply -f 0-mongodb-ns.yaml
```

使用NFS 創建 Volume 需要先把 NFS 資料夾準備好

####2.Create volume
```Bash
$ kubectl -n mongosh apply -f 2-router-volume.yaml

$ kubectl -n mongosh apply -f 2-config1-volume.yaml
$ kubectl -n mongosh apply -f 2-config2-volume.yaml
$ kubectl -n mongosh apply -f 2-config3-volume.yaml

$ kubectl -n mongosh apply -f 2-sh1r1-volume.yaml
$ kubectl -n mongosh apply -f 2-sh1r2-volume.yaml
$ kubectl -n mongosh apply -f 2-sh1r3-volume.yaml

$ kubectl -n mongosh apply -f 2-sh2r1-volume.yaml
$ kubectl -n mongosh apply -f 2-sh2r2-volume.yaml
$ kubectl -n mongosh apply -f 2-sh2r3-volume.yaml

```

####3.Create config server replica set
```Bash
$ kubectl -n mongosh apply -f 3-mongo-config1.yaml
$ kubectl -n mongosh apply -f 3-mongo-config2.yaml
$ kubectl -n mongosh apply -f 3-mongo-config3.yaml
```
Show Pod & SVC
```Bash
$ kubectl -n mongosh get svc
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
config1-svc   ClusterIP   10.99.58.79     <none>        27019/TCP,27017/TCP,27018/TCP   4h34m
config2-svc   ClusterIP   10.109.34.165   <none>        27019/TCP,27017/TCP,27018/TCP   4h34m
config3-svc   ClusterIP   10.106.82.49    <none>        27019/TCP,27017/TCP,27018/TCP   4h34m
$ kubectl -n mongosh get pod
NAME                             READY   STATUS    RESTARTS   AGE
mongo-config1-b5cc456d9-5hs55    1/1     Running   1          157m
mongo-config2-bdc5b6b4b-rwh84    1/1     Running   2          157m
mongo-config3-5d7df9ddf5-p4tqn   1/1     Running   1          157m
```
進入到 config1

```Bash
kubectl -n mongosh exec -it mongo-config1-b5cc456d9-5hs55 bash
# 容器內

mongo mongodb://config1-svc:27019

rs.initiate(
  {
    _id: "Config",
    configsvr: true,
    members: [
      { _id : 0, host : "config1-svc:27019" },
      { _id : 1, host : "config2-svc:27019" },
      { _id : 2, host : "config3-svc:27019" }
    ]
  }
)

#(Enter)
```
跟建立 replic set 一樣，但要多加 configsvr: true。

rs.status() 檢查狀態

####4.Create shard server  replica set
```Bash
$ kubectl -n mongosh apply -f 3-mongo-sh1r1.yaml
$ kubectl -n mongosh apply -f 3-mongo-sh1r2.yaml
$ kubectl -n mongosh apply -f 3-mongo-sh1r3.yaml

$ kubectl -n mongosh apply -f 3-mongo-sh2r1.yaml
$ kubectl -n mongosh apply -f 3-mongo-sh2r2.yaml
$ kubectl -n mongosh apply -f 3-mongo-sh2r3.yaml
```
Show Pod & SVC
```Bash
$ kubectl -n mongosh get svc
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
sh1r1-svc     ClusterIP   10.103.104.88   <none>        27019/TCP,27017/TCP,27018/TCP   4h1m
sh1r2-svc     ClusterIP   10.96.251.126   <none>        27019/TCP,27017/TCP,27018/TCP   3h56m
sh1r3-svc     ClusterIP   10.111.243.93   <none>        27019/TCP,27017/TCP,27018/TCP   3h56m
sh2r1-svc     ClusterIP   10.104.79.106   <none>        27019/TCP,27017/TCP,27018/TCP   3h44m
sh2r2-svc     ClusterIP   10.108.92.71    <none>        27019/TCP,27017/TCP,27018/TCP   3h45m
sh2r3-svc     ClusterIP   10.109.10.217   <none>        27019/TCP,27017/TCP,27018/TCP   3h45m
$ kubectl -n mongosh get pod
NAME                             READY   STATUS    RESTARTS   AGE
mongo-sh1r1-776ff8b466-f5c5z     1/1     Running   0          4h1m
mongo-sh1r2-67444c6b89-hvjwz     1/1     Running   0          3h56m
mongo-sh1r3-c4f68f88-jr9qg       1/1     Running   0          3h56m
mongo-sh2r1-654c6dd94c-z7pvd     1/1     Running   0          3h44m
mongo-sh2r2-56d4bb7d8d-664df     1/1     Running   0          3h45m
mongo-sh2r3-588f9f96cc-2mjxb     1/1     Running   0          3h45m
```

進入到 sh1r1
```Bash
kubectl -n mongosh exec -it mongo-sh1r1-776ff8b466-f5c5z bash
# 容器內
mongo mongodb://sh1r1-svc:27018

rs.initiate(
  {
    _id : "Shard1",
    members: [
      { _id : 0, host : "sh1r1-svc:27018" },
      { _id : 1, host : "sh1r2-svc:27018" },
      { _id : 2, host : "sh1r3-svc:27018" }
    ]
  }
)
#(Enter)
```
rs.status() 檢查狀態

進入到 sh2r1
```Bash
kubectl -n mongosh exec -it mongo-sh2r1-654c6dd94c-z7pvd bash
# 容器內
mongo mongodb://sh2r1-svc:27018

rs.initiate(
  {
    _id : "Shard1",
    members: [
      { _id : 0, host : "sh2r1-svc:27018" },
      { _id : 1, host : "sh2r2-svc:27018" },
      { _id : 2, host : "sh2r3-svc:27018" }
    ]
  }
)
#(Enter)
```
rs.status() 檢查狀態

####5.Create router server-啟動指定 config server 的 router
```Bash
$ kubectl -n mongosh apply -f 1-router-svc.yaml
$ kubectl -n mongosh apply -f 3-mongo-router.yaml
```

Show Pod & SVC
```Bash
$ kubectl -n mongosh get svc
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                         AGE
router-svc    NodePort    10.104.82.81    <none>        27017:30700/TCP                 133m
$ kubectl -n mongosh get pod
NAME                             READY   STATUS    RESTARTS   AGE
mongo-router-675bb97c9-9nmr9     1/1     Running   0          133m
```

進入到 router
```Bash
kubectl -n mongosh exec -it mongo-router-675bb97c9-9nmr9 bash
# 容器內
mongo mongodb://router-svc:27017
#(Enter)
# 加入分片 Shard1 和 Shard2
sh.addShard("Shard1/sh1r1-svc:27018,sh1r2-svc:27018,sh1r3-svc:27018")
sh.addShard("Shard2/sh2r1-svc:27018,sh2r2-svc:27018,sh2r3-svc:27018")
#(Enter)
```
 sh.status() 查詢分片狀態

---

##使用 sharded cluster
我們已經完成建立 sharded cluster，現在連接上 router 就可以當做一般的 standalone 使用。

使用分片功能設定。

####對資料庫開啟 sharding 功能
針對 playground 資料庫開啟 sharding 功能

```Bash
sh.enableSharding("playground")
```
####對集合（collection）開啟分片
開啟資料庫分片功能後，再對需要使用分片的集合 [sh.shardCollection()](https://docs.mongodb.com/manual/reference/method/sh.shardCollection/#mongodb-method-sh.shardCollection "sh.shardCollection()")。

sh.shardCollection(namespace, key) 是最基本的使用方式，namespace 表示是哪個集合要被分片，而 key 是指 Shard Key，其中 shard key 的選擇對於資料的分散策略是很重要的，見：[Choose a Shard Key](https://docs.mongodb.com/manual/core/sharding-choose-a-shard-key/#std-label-sharding-shard-key-selection "Choose a Shard Key")。

我們簡單示範，users 這集合用 hashed index 做為 shard key。
```Bash
sh.shardCollection('playground.users', {name: 'hashed'})
```
接下來，放入兩筆資料 {name: 'user1'}, {name: 'user2'}
```Bash
use playground
db.users.insertMany([{name: 'user1'}, {name: 'user2'}])
```
使用 db.users.getShardDistribution() 查詢分片狀態

在 Totals 區塊中顯示 Shard1, Shard1 分別個放了 50% 的資料，也就剛剛放的資料被平均分散到這二個分片中。

文件參考:
1.https://tw.alphacamp.co/blog/mongodb-with-docker
2.https://docs.mongodb.com/


