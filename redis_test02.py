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
    rc.sadd('sname','s-mysql')
    rc.sadd('sname','s-oracle')
    rc.sadd('sname','s-redis')
    rc.sadd('sname','s-redis')
    rc.sadd('sname','s-mangodb')
    rc.sadd('sname','s-postgres')
    rc.hset('hname','passwd1','test123')
    rc.hset('hname','passwd2','test123')
    rc.hset('hname','passwd1','welcome123')
    rc.zadd('zname','1','apple')
    rc.zadd('zname','2','orange')
    rc.zadd('zname','3','banana')
    rc.zadd('zname','4','lemon')
    rc.zadd('zname','5','banana')
    
    print "name is: ", rc.get('name')
    print "age  is: ", rc.get('age')
    print "set members are: ", rc.smembers('sname')
    print "hash members are: ", rc.hgetall('hname')
    print "zset members are: ", rc.zrange('zname',0,10)

redis_cluster()
