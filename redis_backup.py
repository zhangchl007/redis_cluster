#!/usr/bin/env python
#coding:utf-8

'''
@author: jimmy zhang
'''

from rediscluster import StrictRedisCluster
from time import sleep
from datetime import datetime, timedelta
import sys


def bgsave_and_wait(rc, timeout=timedelta(seconds=60)):

    bgsave_begin = datetime.now()

    t0 = rc.lastsave()
    if rc.bgsave():
        while True:
            if rc.lastsave() != t0:
                break
            if datetime.now() - bgsave_begin > timeout:
                return 'timeout'
            sleep(1)
        return 'ok'
    else:
        return 'failed'


if __name__ == '__main__':

     redis_nodes =  [{'host':'192.168.122.9','port':7000},
                    {'host':'192.168.122.8','port':7001},
                    {'host':'192.168.122.7','port':7002},
                    {'host':'192.168.122.6','port':7003},
                    {'host':'192.168.122.5','port':7004},
                    {'host':'192.168.122.4','port':7005}
                   ]

     try:
         rc = StrictRedisCluster(startup_nodes=redis_nodes, decode_responses=True, password='test123')
     except Exception,e:
         print "Connect Error!"
         sys.exit(1)

     bgsave_and_wait(rc)

