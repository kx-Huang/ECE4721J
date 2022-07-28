# VE472 Project cluster setup SU2022
## General info
1. Machine info: https://focs.ji.sjtu.edu.cn/git/TAs/ve472/issues/5
2. Docker configurations: Forked from Yihao's project https://github.com/xiejinglei/hadoop-cluster
3. (Different from files in previous years! Please make changes in Dockerfile and download.sh if you clone a new one) Make sure the versions exist in tsinghua's mirror. May need to change `Dockerfile` and `download.sh`. In SU2022, we use
    ```
    HADOOP_VERSION=3.3.2
    DRILL_VERSION=1.20.0
    ZOOKEEPER_VERSION=3.8.0
    SPARK_VERSION=3.3.0
    ```
4. Some configurations of zookeeper and drill has been changed.


## Test on single server
1. Install git. Clone repo `hadoop-cluster`.
2. Install docker: `install-docker.sh`
3. ssh:
    ```bash
    ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    ```
    At `hadoop-cluster`,
    ```bash
    mkdir -p .config && cp ~/.ssh/{id_rsa,id_rsa.pub} .config
    ```
4. Build docker image
    ```bash
    ./download.sh
    ./build/docker-build-image.sh
    ```
    (If network fails, rerunning build may solve the problem)
5. Hadoop network
    ```bash
    docker system prune
    master/init_swarm.sh
    master/init_network.sh
    ```
    `docker network ls` gives
    ```
    docker network ls
    NETWORK ID     NAME              DRIVER    SCOPE
    8bd0d2f2a680   bridge            bridge    local
    3c96dadc7b05   docker_gwbridge   bridge    local
    kx2x2si4xgvz   hadoop-net        overlay   swarm
    063c6f637672   host              host      local
    d88xmyyob83a   ingress           overlay   swarm
    0bc2911e33f1   none              null      local
    ```
6. Start containers
    ```
    ./standalone.sh
    ```
7. Check hdfs status in `hadoop-master`
    ```
    hdfs fsck /
    hadoop dfsadmin -report
    ```
    Check yarn status
    ```
    yarn top
    ```
    Or use web dashboard:
    ```
    ### status
    http://<IP_MASTER>:8088/
    http://<IP_MASTER>:9870/
    ```



## Deploy over cluster
1. Initialization: (Already cloned in root directory. Notice the version problem!)
    ```bash
    apt-get update && apt install -y git
    git clone https://github.com/xiejinglei/hadoop-cluster.git
    git clone https://github.com/xiejinglei/hadoop-eco.git
    bash ~/hadoop-eco/project-cluster/install-docker.sh
    ```
2. ssh:
    ```bash
    ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
    ```
    At `hadoop-cluster`,
    ```bash
    mkdir -p .config && cp ~/.ssh/{id_rsa,id_rsa.pub} .config
    ```
3. Build docker image
    ```bash
    ./download.sh
    ./build/docker-build-image.sh
    ```
    (If network fails, rerunning build may solve the problem)
4. Copy the image to all machines.
5. Configure network:

   On network manager node,
   ```bash
    docker system prune
    master/init_swarm.sh
    master/init_network.sh
    ```
    note (7/22/2021)
    ```bash
    docker swarm join --token SWMTKN-1-1k9taznxwmh32ec4pf3vmbdjl50339c5umez2kkuro857ugw6j-3auj14y2w43umk0qg1blfause 192.168.3.8:2377
    ```
    On workers,
    ```bash
    docker system prune
    worker/join_swarm.sh <TOKEN> <IP-ADDRESS-OF-MANAGER>
    ```
    And then paste the command generated in manager.
6. Start containers

    On master node,
    ```bash
    export WORKER_NUMBER=7
    master/start.sh
    ```
    On `worker-n`, start a detached (-d) and interactive (-it) container `hadoop-worker-n` that connects to `hadoop-net`.

    Mapping:

    `ve472-hadoop-2` -> `WORKER_ID=1`
    ...

    `ve472-hadoop-8` -> `WORKER_ID=7`
    ```bash
    export WORKER_NUMBER=7
    export WORKER_ID=X
    worker/start.sh
    ```
7. Start `NameNode` daemon, `DataNode` daemon, `ResourceManager` daemon and `NodeManager` daemon in `hadoop-master` container.

    ```bash
    master/start_hadoop.sh
    ```
    Check `jps` to see if the services have been started.

    Run sample task:
    ```bash
    ./run-wordcount.sh
    ```
8. Now we can check yarn status from our own laptop
    ```
    http://10.119.6.238:8088/
    ```
    where `10.119.6.238` is master's public IP. Also check hdfs at
    ```
    http://10.119.6.238:9870/
    ```
    Note: make sure to open the ports 9870 and 8088 on the host machine. Container ports are mapped to host ports.
9. Testing drill
    Go to `$DRILL_HOME` and run `bin/drill-conf`. Should see
    ```
    Apache Drill 1.18.0
    "Drill never goes out of style."
    apache drill>
    ```
    Check drillbit status
    ```sql
    apache drill> SELECT * FROM sys.drillbits;
    +-----------------+-----------+--------------+-----------+-----------+---------+---------+--------+
    |    hostname     | user_port | control_port | data_port | http_port | current | version | state  |
    +-----------------+-----------+--------------+-----------+-----------+---------+---------+--------+
    | hadoop-worker-4 | 31010     | 31011        | 31012     | 8047      | true    | 1.18.0  | ONLINE |
    | hadoop-worker-3 | 31010     | 31011        | 31012     | 8047      | false   | 1.18.0  | ONLINE |
    | hadoop-worker-6 | 31010     | 31011        | 31012     | 8047      | false   | 1.18.0  | ONLINE |
    | hadoop-worker-5 | 31010     | 31011        | 31012     | 8047      | false   | 1.18.0  | ONLINE |
    | hadoop-master   | 31010     | 31011        | 31012     | 8047      | false   | 1.18.0  | ONLINE |
    | hadoop-worker-2 | 31010     | 31011        | 31012     | 8047      | false   | 1.18.0  | ONLINE |
    | hadoop-worker-1 | 31010     | 31011        | 31012     | 8047      | false   | 1.18.0  | ONLINE |
    | hadoop-worker-7 | 31010     | 31011        | 31012     | 8047      | false   | 1.18.0  | ONLINE |
    +-----------------+-----------+--------------+-----------+-----------+---------+---------+--------+
    ```
    If there is any drillbit not working, go to the corresponding container and check its status. See `trouble-shooting`.


## Mount data
Mount server file system:
```bash
sshfs -o port=2223 -o allow_other ve472@focs.ji.sjtu.edu.cn: .disk/
```
Unmount:
```bash
fusermount -u .disk/
```
Mount the iso file:
```bash
mkdir d
mount -o loop .disk/millionsong.iso d
```


## Trouble shooting
1. Remove all containers:
   ```
   docker rm -f $(docker ps -aq)
   ```

2. Error when starting master container
   ```
   Error starting userland proxy: listen tcp4 0.0.0.0:22: bind: address already in use
   ```
   Solved by changing `master/docker-compose.yml`
    ```yml
    ports:
      - "9870:9870"
      - "8088:8088"
      - "8047:8047"
      - "19888:19888"
      - "2224:22"           <- this line
    ```
3. Spark may need to set environment variables
    ```
    export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop
    ```
4. If worker cannot join swarm, and
    ```bash
    telnet <ip-of-manager> 2377
    ```
    cannot be reached, then the port 2377 might haven been blocked on manager. Necessary ports for overlay network: https://docs.docker.com/network/overlay/
    ```bash
    apt-get install ufw
    ufw allow 2377
    ufw allow 7946
    ufw allow 4789
    ```
    Check the result:
    ```bash
    netstat -tulpn
    ```
    If still cannot reach, may ask IT to open the port.
5. Check drillbit status: go to `bin`
    ```bash
    ./drillbit.sh status
    ```
    If not running, may need to start drillbit manually.
    ```bash
    ./drillbit.sh start
    ```
6. Environment variables
    ```bash
    # Java
    export JDK_VERSION=8
    export JAVA_HOME=/usr/lib/jvm/java-${JDK_VERSION}-openjdk-amd64

    # Hadoop
    export HADOOP_HOME=/usr/local/hadoop
    export HADOOP_CLASSPATH=${JAVA_HOME}/lib/tools.jar:${HADOOP_CLASSPATH}
    export PATH=${JAVA_HOME}/bin:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:${PATH}
    export LD_LIBRARY_PATH=${HADOOP_HOME}/lib/native

    # Drill
    export DRILL_HOME=/usr/local/drill
    export PATH=${DRILL_HOME}/bin:${PATH}

    # Zookeeper
    export ZOOKEEPER_HOME=/usr/local/zookeeper
    export PATH=${ZOOKEEPER_HOME}/bin:${PATH}

    # Spark
    export SPARK_HOME=/usr/local/spark
    export PATH=${SPARK_HOME}/bin:${PATH}
    export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop
    ```
6. Grant permission in hdfs
    ```bash
    hadoop fs -chown -R pgroup1:pgroup1 /user/pgroup1
    ```
7. Mount home:
    ```bash
    /var/lib/docker/volumes/hadoop-master_home/_data
    ```
8. Drill check schema
    ```sql
    describe schema dfs;
    ```
