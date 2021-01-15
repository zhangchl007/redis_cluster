#!/usr/bin/env python
#coding:utf-8

'''
@author: jimmy zhang
'''

from rediscluster import RedisCluster
from multiprocessing import Pool
import sys

def redis_cluster(i):
    redis_nodes =  [{'host':'redis-master','port':6379}]
    try:
        #redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
        redisconn = RedisCluster(startup_nodes=redis_nodes, decode_responses=True, password='Opstree@1234')
    except Exception as e:
        print("Connect Error!")
        sys.exit(1)

    key='foo'+ str(i)
    redisconn.set(key, i)
    print("key:%s ==> value:%s" %(key,redisconn.get(key)))

if __name__ == '__main__':
     list = range(50000000)
     with Pool(processes=20) as pool:
         pool.map_async(redis_cluster, list)
         pool.close()
         pool.join()
