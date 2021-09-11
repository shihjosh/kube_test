#!/bin/bash
#Add shard to router 

router_pod1=mongosrouter-0
router_container1=mongosroutercontainer
shardreplicaset=mongoreplicaset1shard
mongoport=27017
declare -a shard1pod

 echo "Get fqdn for shards and config replicaset..."
 #Get FQDN for shard replicaset
 num=0
 shardarray=(`kubectl -n mongoshard get --no-headers=true pods -l role=mongoshard -o custom-columns=:metadata.name`)
 for i in ${shardarray[@]};do
  echo $i
  shard1pod[num++]=`kubectl -n mongoshard exec $i -- hostname -f`
 done


 #Add Shards on routers
  echo "Configure router to be aware of the Shards, performing addshard().."
  kubectl -n mongoshard exec ${router_pod1}  -c ${router_container1} -- bash -c "echo 'sh.addShard(\"${shardreplicaset}/${shard1pod[0]}:${mongoport}\")' |mongo "
  echo "Adding shard completed on routers"
  sleep 3
  kubectl -n mongoshard exec ${router_pod1} -c ${router_container1} -- mongo --eval 'sh.status()'


