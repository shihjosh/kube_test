## K8s Demo

前置作業:
- 安裝 AWS CLI
- 安裝 eksctl
- 安裝 kubectl

創建 IAM:
- 具有 創建 EKS 權限
- 具有 創建 EC2 權限

---
##### create EKS cluster
```Bash
$eksctl create cluster \
--name test-cluster \
--version 1.18 \
--region ap-northeast-1 \ #東京伺服器
--nodegroup-name linux-nodes \
--node-type t2.micro \ # EC2
--nodes 2  # 開啟幾台
```

1.Create Namespace
```Bash
$ kubectl apply -f namespaces.yaml
```
2.Create some resources
```Bash
$ kubectl apply -n example-app -f secrets.yaml
$ kubectl apply -n example-app -f configmap.yaml
$ kubectl apply -n example-app -f deployment.yaml
```
3.change the `type: LoadBalancer`
```Bash
$ kubectl apply -n example-app -f service.yaml
```
## 驗證
```Bash
$ kubectl get svc -n example-app
```
利用網頁連線 EXTERNAL-IP

##### Delete EKS cluster
```Bash
$ eksctl delete cluster --name test-cluster
```