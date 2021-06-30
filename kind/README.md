# 安裝 kind

環境:
- ubuntu 20.04 LTS

```bash
#系統更新
$ sudo apt update
$ sudo apt upgrade
$ sudo apt autoremove
$ sudo apt install net-tools
$ sudo apt install openssh-server
$ sudo apt install curl
$ sudo apt install vim
$ sudo apt install git
```

```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && sudo apt-get install docker-ce -y
$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
$ wget https://golang.org/dl/go1.15.8.linux-amd64.tar.gz && sudo tar -C /usr/local -xzf go1.15.8.linux-amd64.tar.gz && export PATH=$PATH:/usr/local/go/bin
$ GO111MODULE="on" go get sigs.k8s.io/kind@v0.10.0 && sudo su
$ export PATH=$PATH:/home/<user>/go/bin <---check /home/<user>/go/bin
$ kind create cluster
$ kind get clusters && kubectl cluster-info --context kind-kind
$ kubectl run mypod --image=nginx && kubectl get pods -w
```

```
$ curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.11.1/kind-linux-amd64
$ chmod +x ./kind
$ mv ./kind /usr/local/bin/kind
```

把目前使用者加到docker群組裡面, 當docker service 起來時, 會以這個群組的成員來初始化相關服務

```Bash
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
```

基本指令
```Bash
$ kind create cluster # 創建集群
$ kind delete cluster # 刪除集群
$ kind create cluster --config kind-example-config.yaml # 創建自訂集群
```


https://kind.sigs.k8s.io/

kindest/node:
https://github.com/kubernetes-sigs/kind/releases
