from kazoo.client import KazooClient
from kazoo.client import KazooState
import time
import json
# Establishing connection to Zookeeper node
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()


if zk.state == KazooState.CONNECTED:
    # creating nodes
    if zk.exists("/client-1"):
        zk.delete("/client-1")