## K8s Demo

前置作業:
安裝 AWS CLI
安裝 eksctl
安裝 kubectl

創建 IAM:
具有 創建 EKS 權限
具有 創建 EC2 權限

建立 EKS cluster 所需權限
從 IAM 中建立一個 role，而這個 role 的功能是要套用在 EKS cluster 身上，並賦予其有足夠的權限去操控其他的 AWS 資源，達成自動化管理相關 AWS resource 的目的，流程如下：
1. 進入 IAM console，選擇 Role -> Create role
2. trusted entity 選擇 AWS service，use case 則是選擇 EKS cluster
3. 設定 tag & review(如果有需要)，最後則是輸入一個 unique role name(例如 eksClusterRole)，到這邊就完成了 role 的建立

---

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
