## K8s Demo

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