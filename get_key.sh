#!/bin/bash
redis-cli -h 192.168.122.9 -p 7000 -a test123  --scan --pattern '*'
redis-cli -h 192.168.122.8 -p 7001 -a test123  --scan --pattern '*'
redis-cli -h 192.168.122.7 -p 7002 -a test123  --scan --pattern '*'
redis-cli -h 192.168.122.6 -p 7003 -a test123  --scan --pattern '*'
redis-cli -h 192.168.122.5 -p 7004 -a test123  --scan --pattern '*'
redis-cli -h 192.168.122.4 -p 7005 -a test123  --scan --pattern '*'
