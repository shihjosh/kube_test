# 安裝監控

環境:
- ubuntu 20.04 LTS
- prometheus
- grafana
- node_exporter

prometheus.yml 檔案 根據 localhost/或其他監測IP 替換

RUN docker-compose
```bash
$ docker-compose up -d
```

登入 grafana
1.設定密碼
2.設定資料來源
3.import 模板
4.選擇資料來源