from kazoo.client import KazooClient
from kazoo.client import KazooState
import time
import json
# Establishing connection to Zookeeper node
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# Client Data
SERVICE_CONFIG = {"client_name": "client-1"}

# converting data to bytes
SERVICE_CONFIG = json.dumps(SERVICE_CONFIG).encode("utf-8")

if zk.state == KazooState.CONNECTED:  # check connection state with zookeeper node

    # creating nodes
    if not zk.exists("/client-1"):
        zk.create("/client-1")

    # configuring data on a zookeeper node
    zk.set("/client-1", SERVICE_CONFIG)