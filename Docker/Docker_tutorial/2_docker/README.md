# 映像檔(Images)
Docker 映像檔(Image)就是一個唯讀的模板(template)。

EX：一個映像檔(Image)可以包含一個完整的 Ubuntu 作業系統環境 或 windows server，裡面安裝了 Apache 或使用者需要的其它應用程式。

映像檔可以用來建立 Docker 容器(Container)。

Docker Hub 有非常多已建立好的映像檔(Images)可以直接使用。

# 容器(Container)

Docker 利用容器(Container)來執行應用。

容器(Container)是從映像檔(Image)建立的執行實例。

它可以被啟動、開始、停止、刪除。每個容器都是相互隔離的、保證安全的平台。
可以把容器看做是一個簡易版的 Linux/windows server 環境（包括root使用者權限、程式空間、使用者空間和網路空間等）和在其中執行的應用程式。

*註：映像檔是唯讀的，容器在啟動的時候建立一層可寫層作為最上層。

# 倉庫（Repository）

倉庫（Repository）是集中存放映像檔(Images)檔案的場所。

實際上，倉庫註冊伺服器上往往存放著多個倉庫，每個倉庫中又包含了多個映像檔(Images)，每個映像檔(Image)有不同的標籤（tag）。

倉庫分為公開倉庫（Public）和私有倉庫（Private）兩種形式。

最大的公開倉庫是 Docker Hub，存放了大量映像檔(Image)供使用者下載。 

當然，使用者也可以在本地網路內建立一個私有倉庫 (Nexus 3)。

當使用者建立了自己的映像檔之後就可以使用 push 命令將它上傳到公有或者私有倉庫，這樣下次在另外一台機器上使用這個映像檔時候，只需要從倉庫上 pull 下來就可以了。


