#!/bin/bash

#Cleanup the Shard replicaset
#for i in 0 1 2 3 4 5
#do
 #kubectl -n mongoshard exec mongodbshardstateful-${i} -c mongodshardcontainer -- bash -c "rm -rfd /data/db"
#done 

kubectl -n mongoshard delete statefulsets mongodbshardstateful
kubectl -n mongoshard delete services mongodbshardservice

kubectl -n mongoshard delete statefulsets mongodbshardstateful2
kubectl -n mongoshard delete services mongodbshardservice2

kubectl -n mongoshard delete pvc -l role=mongoshard
#kubectl -n mongoshard delete pods mongodshard-0 --grace-period=0 --force


#Cleanup the config replicaset
#for i in 0 1 2 3 4 5
#do
 #kubectl -n mongoshard exec mongodbconfigstateful-${i} -c mongodshardcontainer -- bash -c "rm -rfd /data/db"
#done 

#Cleanup the Config replicaset
kubectl -n mongoshard delete statefulsets mongodbconfigstateful
kubectl -n mongoshard delete services mongodbconfigservice

kubectl -n mongoshard delete pvc -l role=mongoconfig

#Cleanup the Routers
kubectl -n mongoshard delete statefulsets mongosrouter
kubectl -n mongoshard delete services mongodbroutersvc

