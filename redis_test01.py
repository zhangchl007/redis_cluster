#!/usr/bin/env python
#coding:utf-8

'''
@author: jimmy zhang
'''

from rediscluster import StrictRedisCluster
import sys

def redis_cluster():
    redis_nodes =  [{'host':'192.168.122.9','port':7000},
                    {'host':'192.168.122.8','port':7001},
                    {'host':'192.168.122.7','port':7002},
                    {'host':'192.168.122.6','port':7003},
                    {'host':'192.168.122.5','port':7004},
                    {'host':'192.168.122.4','port':7005}
                   ]
    try:
        #rc = StrictRedisCluster(startup_nodes=redis_nodes)
        rc = StrictRedisCluster(startup_nodes=redis_nodes, decode_responses=True, password='test123')
    except Exception,e:
        print "Connect Error!"
        sys.exit(1)

    rc.set('name','admin')
    rc.set('age',18)
    rc.lpush('lname','oracle')
    rc.lpush('lname','mysql')
    rc.lpush('lname','mongodb')
    
    print "name is: ", rc.get('name')
    print "age  is: ", rc.get('age')
    print "list  is: ", rc.lrange('lname',0,100)

if __name__ == '__main__':
    redis_cluster()
