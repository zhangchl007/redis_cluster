#!/bin/bash
host=`hostname`

if [ $host="redis01" ]; then
    cd /opt/redis/cluster-test/
    nohup  ./redis-server /opt/redis/cluster-test/7000/redis.conf &
elif  [ $host="redis02" ]; then
    cd /opt/redis/cluster-test/
    nohup  ./redis-server /opt/redis/cluster-test/7001/redis.conf &
elif  [ $host="redis03" ]; then
    cd /opt/redis/cluster-test/
    nohup ./redis-server /opt/redis/cluster-test/7002/redis.conf &
elif  [ $host="redis04" ]; then
    cd /opt/redis/cluster-test/
    nohup ./redis-server /opt/redis/cluster-test/7003/redis.conf &
elif  [ $host="redis05" ]; then
    cd /opt/redis/cluster-test/
    nohup ./redis-server /opt/redis/cluster-test/7004/redis.conf &
elif  [ $host="redis06" ]; then
    cd /opt/redis/cluster-test/
    nohup ./redis-server /opt/redis/cluster-test/7005/redis.conf &
else

     echo "redis start failed"
fi 
