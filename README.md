# Apache Zookeeper Demo

## Overview

This repository hold manifests for Zookeeper demo.

## Details:

1. These files are required for the demo.
```bash
├── add-configuration.py # it will create a data node and add configuration on that node.
├── delete-node.py # it will delete the data node 
├── distributed-system-service.py # it will extract data from the data node
└── update_configuration.py # it will update the data node.
```

2. Start Zookeeper service:
    
    * [Download](https://zookeeper.apache.org/releases.html#download) Zookeeper binaries.
    
    * Extract the content:
    ```bash
    tar -xvf apache-zookeeper-x.x.x-bin.tar.gz
    ```

    * Rename the default zookeeper config file. It is available in `apache-zookeeper-x.x.x-bin/conf` folder:
    ```bash
    mv zoo_sample.cfg zoo.cfg
    ```

    * Start the service using the command given below:
    ```bash
    # move inside the folder containing zookeeper manifests
    cd apache-zookeeper-x.x.x-bin

    # start the service
    sudo ./bin/zkServer.sh start
    ```

    * To stop the service use the command given below:
    ```bash
    sudo ./bin/zkServer.sh stop
    ```

3. Install python3.

4. Install required python3 modules:
```bash
python3 install -r requirements.txt
```

5. Now start the distributed system's service:
```bash
python3 distributed-system-service.py
```
It will perform following tasks:

    * It will check whether the data node is created or not, after a defined interval of 5 seconds.
    * Once data node is created it will populate SERVICE_CONFIG dict with the data on the node.
    * It will add watch method on the data node to update the SERVICE_CONFIG if any changed is occurred on the data node.
    * It will continue to print the SERVICE_CONFIG on terminal.

6. Create a data node and populate it with data:
```bash
python3 add-configuration.py
```

7. When the data node is created and populated with data the change can be seen in the service logs on terminal that was started in previous step.

8. Update the data on the node:

```bash
python3 update_configuration.py
```
If data node is updated successfully it can be seen in the service logs that the config is also updated.

9. Delete the data node:
```bash
python3 delete-node.py
```