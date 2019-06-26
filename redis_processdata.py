#!/usr/bin/env python
#coding:utf-8

'''
@author: jimmy zhang
'''

from rediscluster import StrictRedisCluster
import sys

def redis_cluster():
    redis_nodes =  [{'host':'192.168.122.9','port':7000}]
    try:
        #redisconn = StrictRedisCluster(startup_nodes=redis_nodes)
        redisconn = StrictRedisCluster(startup_nodes=redis_nodes, decode_responses=True, password='test123')
    except Exception,e:
        print "Connect Error!"
        sys.exit(1)

    for  i in range(0,5000):
          
        key='foo'+ str(i)
        redisconn.set(key, i)
        print 'key:%s ==> value:%s'  %(key,redisconn.get(key))

if __name__ == '__main__':
    redis_cluster()
