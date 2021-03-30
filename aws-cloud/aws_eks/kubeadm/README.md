# kubeadm

[Install Kubernetes Cluster using kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)

kubectl adm Tutorial -github

---

- Verify the MAC address and product_uuid are unique for every node

3個ubuntu 環境都是分別裝起來 避免 kubeadm 不必要的衝突

---

環境:Oracle VM VirtualBox 6.1

- master-ubuntu-desktop 20.04 LTS版
- node01-ubuntu-desktop 20.04 LTS版
- node02-ubuntu-desktop 20.04 LTS版

|  Role |  IP(根據分到的IP) |  OS |  RAM |  CPU |
| ------------ | ------------ | ------------ | ------------ | ------------ |
|  Master | 192.168.11.136  | ubuntu 20.04 LTS  | 2G |  2 |
| node01  | 192.168.11.138  |  ubuntu 20.04 LTS  | 2G |  2 |
| node02  | 192.168.11.139 |   ubuntu 20.04 LTS | 2G |  2 |

```
工具版本
docker-ce=5:19.03.10~3-0~ubuntu-focal  //apt-cache madison docker-ce  會查到其他版本資訊
kubeadm=1.18.5-00 
kubelet=1.18.5-00 
kubectl=1.18.5-00
```

Oracle VM VirtualBox 6.1 主要設定:

網路 介面卡

附加到: 橋接介面卡(模擬真實主機狀態)

- 使用root 權限

```
$ sudo -i
```

1.關掉防火牆(ufw disable)

```
$ ufw disable
```

2.關閉虛擬記憶體(Disable swap)

```
$ swapoff -a
$ sed -i '/swap/d' /etc/fstab
```

3.更新 Kubernetes network 系統設定

```
cat >>/etc/sysctl.d/kubernetes.conf<<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF
sysctl --system
```

4.安裝 Docker engine (Install docker engine)

```
$ apt install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
$ add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ apt update
$ apt install -y docker-ce=5:19.03.10~3-0~ubuntu-focal containerd.io
```

### Kubernetes Setup

5.Add Apt repository

```
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
$ echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
```

6.Install Kubernetes components

```
$ apt update && apt install -y kubeadm=1.18.5-00 kubelet=1.18.5-00 kubectl=1.18.5-00
$ apt-mark hold kubelet kubeadm kubectl
```

- *以上是所有機器需要做的事情

---

On Master-(只有Master 主機需要安裝)

### Initialize Kubernetes Cluster

1.Update the below command with the ip address of master

```
$ sudo kubeadm init --apiserver-advertise-address=192.168.11.136 --pod-network-cidr=192.168.0.0/16  --ignore-preflight-errors=all
```

CNI Plugin: (主要基本功能提供 Pod x Pod 連線 )

Calico CNI (Container Network Interface):**192.168.0.0/16  (本次使用)**

**Calico=>除了基本功能,還有提供其他功能**

Flannel CNI:**10.244.0.0/16**

### **2.**Deploy Calico network

```
$ sudo kubectl --kubeconfig=/etc/kubernetes/admin.conf create -f https://docs.projectcalico.org/v3.14/manifests/calico.yaml
```

3.Cluster join command -如果忘記紀錄 Join master 指令 可以輸入這段找回

```
$ sudo kubeadm token create --print-join-command
```

4. To be able to run kubectl commands as non-root user

```
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

---

NODE-(其他節點加入Master)

將節點加入 Master

指令是 Master 產生 貼在ubuntu-NODE 執行

```
$ kubeadm join 192.168.11.136:6443 --token aujovi.2ewddfc9ypkqfbp0  --discovery-token-ca-cert-hash sha256:d70c148ac96428574fa146ccf90bf8a3fdb806fdba4bc3766509065f3645b57a
```

如果沒記錄到在ubuntu-Master 輸入以下指令找回:

```
$ sudo kubeadm token create --print-join-command
```

完成圖:

測試:

kubeadm 預設Master是不執行Pod工作，如果需要可以下指令一起分安工作

```
//所有主伺服器都安排 pod
$ kubectl taint nodes --all node-role.kubernetes.io/master-
//指定節點 master 伺服器都安排 pod
$ kubectl taint nodes <master-hostname> node-role.kubernetes.io/master-
ex：kubectl taint nodes master node-role.kubernetes.io/master-
```

deployment-test:

```
kubectl create deployment nginx --image=nginx:1.7.9
```

如圖:

Master-

node01-docker 會看到 deploument 的 nginx

其他設定:

將 node01 & node02 ROLES 標記 worker

```
$ kubectl label node <node_name> node-role.kubernetes.io/worker=worker
node/<node_name> labeled

EX:
$ kubectl label node node01 node-role.kubernetes.io/worker=worker
node/node01 labeled
$ kubectl label node node02 node-role.kubernetes.io/worker=worker
node/node02 labeled
```

如果 worker節點加入 master 時配置有問題可以在 worker節點上使用 kubeadm reset 重置配置再使用 kubeadm join 命令重新加入即可。

```
$ kubeadm reset
```

希望在 master 節點刪除 node ，可以使用 kubeadm delete nodes 刪除。

```
$ kubeadm delete nodes
```