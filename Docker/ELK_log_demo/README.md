
# 安裝 ELK 測試

環境:
- ubuntu 20.04 LTS

```bash
docker-compose up -d
```

link kibana web:
http://127.0.0.1:5601/ 

To: 
  Management
   -> Dev Tools

-輸入測試
```bash
GET /_cat/indices

GET hello-logstash-docker/_search
{
  "query": {
    "match_all": {}
  }
}
```

- 開一個新中端機測試
```bash
telnet localhost 5000
hello
test001
test02
```

再到網頁
  Management
   -> Dev Tools

查看有沒有資料

# 測試後目標整合所有為服務的 logs files 方便查錯

From:
  https://www.youtube.com/watch?v=I2ZS2Wlk1No

