# 安裝 Docker Mariadb Spider Storage Engine

環境:
- ubuntu 20.04 LTS


進入每個DB容器設定修改 50-server.cnf
```bash
#設定修改 50-server.cnf
cd /etc/mysql/mariadb.conf.d

----
echo '
[server]
[mysqld]
pid-file                = /run/mysqld/mysqld.pid
basedir                 = /usr
datadir                 = /var/lib/mysql
tmpdir                  = /tmp
lc-messages-dir         = /usr/share/mysql
lc-messages             = en_US
skip-external-locking
bind-address            = 0.0.0.0
expire_logs_days        = 10
character-set-server  = utf8mb4
collation-server      = utf8mb4_general_ci
[embedded]
[mariadb]
[mariadb-10.7]
' > /etc/mysql/mariadb.conf.d/50-server.cnf
```

進入 mariadbspider 的容器，在裡面安裝 Spider 插件：
```bash
#安裝系統依賴包
apt update
apt install mariadb-plugin-spider
```

配置 spider

進入 mariadbspider 的容器，執行以下命令，加載 spider 插件，將其設置為 Spider 數據庫實例。
```bash
INSTALL SONAME 'ha_spider';
-----
檢查是否啟動

SELECT * FROM mysql.plugin;
```
Create the spider table on the Spider Node:
```bash
CREATE SERVER mariadb1 
  FOREIGN DATA WRAPPER mysql 
OPTIONS( 
  HOST 'mariadb1', 
  DATABASE 'test1',
  USER 'root',
  PASSWORD '123456',
  PORT 3306
);
CREATE SERVER mariadb2
  FOREIGN DATA WRAPPER mysql 
OPTIONS( 
  HOST 'mariadb2', 
  DATABASE 'test1',
  USER 'root',
  PASSWORD '123456',
  PORT 3306
);
CREATE SERVER mariadb3
  FOREIGN DATA WRAPPER mysql 
OPTIONS( 
  HOST 'mariadb3', 
  DATABASE 'test1',
  USER 'root',
  PASSWORD '123456',
  PORT 3306
);
CREATE DATABASE IF NOT EXISTS test1;
CREATE  TABLE test1.sbtest
(
  id int(10) unsigned NOT NULL AUTO_INCREMENT,
  k int(10) unsigned NOT NULL DEFAULT '0',
  c char(120) NOT NULL DEFAULT '',
  pad char(60) NOT NULL DEFAULT '',
  PRIMARY KEY (id),
  KEY k (k)
) ENGINE=spider COMMENT='wrapper "mysql", table "sbtest"'
 PARTITION BY KEY (id) 
(
 PARTITION pt1 COMMENT = 'srv "mariadb_1"',
 PARTITION pt2 COMMENT = 'srv "mariadb_2"',
 PARTITION pt3 COMMENT = 'srv "mariadb_3"' 
) ;

-----其他節點也要建
CREATE DATABASE IF NOT EXISTS test1;
CREATE  TABLE test1.sbtest
(
  id int(10) unsigned NOT NULL AUTO_INCREMENT,
  k int(10) unsigned NOT NULL DEFAULT '0',
  c char(120) NOT NULL DEFAULT '',
  pad char(60) NOT NULL DEFAULT '',
  PRIMARY KEY (id),
  KEY k (k)
)
```

