# Redis cluster 驗證

```bash
$ docker exec -it redis-node3 redis-cli -p 9003 -c set k4 v4
OK

$ docker exec -it redis-node3 redis-cli -p 9003 -c
127.0.0.1:9003> set k4 v4
-> Redirected to slot [8455] located at 192.168.100.4:9002
OK
```