# redis-cluster-manager
Python scripts for managing Redis Cluster, including creating, starting and stoping the cluster.

Usage:
- copy redis-server and redis-trib.rb to this directory or create links
- create cluster.json and redis.conf
- run init.py on every node
- run start.py on every node to start the processes
- run create.py on one node to create the cluster
- run stop.py on every node to stop the processes

Tested with RHEL 6.6 and Python 3.4
