from kazoo.client import KazooClient
from kazoo.client import KazooState
import time
import json


# CONSTANTS
SERVICE_CONFIG_PATH = "/client-1"
global SERVICE_CONFIG
SERVICE_CONFIG = {"config": None}

# Creating connection with Zookeeper
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()


# A method that will be trigerred when there is a change on the node where watch
# is configured.
def watcher_method(event):
    data, stat = zk.get(SERVICE_CONFIG_PATH, watch=watcher_method)
    SERVICE_CONFIG["config"] = json.loads(data.decode("utf-8"))
    print("Data has been updated")
    print("Version: %s, data: %s" % (stat.version, SERVICE_CONFIG))


# check connection state
if zk.state == KazooState.CONNECTED:
    # this loop will continue to run until data node is not created.
    while True:
        if zk.exists(SERVICE_CONFIG_PATH):
            print("Data Node is available")
            data, stat = zk.get(SERVICE_CONFIG_PATH, watch=watcher_method)
            SERVICE_CONFIG["config"] = json.loads(data.decode("utf-8"))
            print("Version: %s, data: %s" % (stat.version, SERVICE_CONFIG))
            break
        else:
            print("Data Node is not available")
        time.sleep(5)

# This loop will print the config
while True:
    print(SERVICE_CONFIG, "\n")
    time.sleep(5)
