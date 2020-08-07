from kazoo.client import KazooClient
from kazoo.client import KazooState
import time
import json
# Establishing connection to Zookeeper node
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

SERVICE_CONFIG = {"client_name": "client-2"}

zk.set("/client-1", json.dumps(SERVICE_CONFIG).encode("utf-8"))