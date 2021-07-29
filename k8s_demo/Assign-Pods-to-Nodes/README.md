# Assign-Pods-to-Nodes

環境:
- ubuntu 20.04 LTS
- kind

1. 給Nodes添加labe

```bash
#列出集群中的Node
$ kubectl get nodes
```

2.選擇其中一個Node，為它添加labe：

```bash
$ kubectl label nodes <your-node-name> disktype=ssd
```

3.驗證你選擇的Node是否有 disktype=ssd

```bash
$  kubectl get nodes --show-labels
```

4.創建一個調度到你選擇的節點的pod

```
$  kubectl apply -f 1-demo.yaml

```

5.驗證pod 是不是運行在你選擇的節點上

```
$  kubectl get pods -o wide

```
