# VE472 Lab 5: Larger cluster

Goals:
- Scale up a cluster
- Run a heavy computation over the cluster
- Observe the benefits of using `Hadoop`

## I. Preparation

We will take advantage of `docker` to deploy to whole cluster.

`Docker` is a set of platform as a service products that use OS-level virtualization to deliver software in packages called `containers`.

- `Image`: contains application code, libraries, tools, dependencies and other files needed to make an application run.
- `Container`: Runs tha application in a light-weight manner

Please refer this [Github Repo](https://github.com/tc-imba/hadoop-cluster)^[thanks to [`Boming`](https://github.com/BoYanZh) for his contribution], and we can deploy everything we need in a quick and easy way.

*Note: docker commands may need `sudo`.*

Steps:

1. Download and install docker: `https://docs.docker.com/engine/install/ubuntu/` (ubuntu example)
2. Obtain docker image

    - Docker images can be built from Dockerfile or obtained from docker hub repos. To save time, we have provided the Dockerfile for you in the git repo. (Make sure you have enough space on your disk.)

    - After building, You may check the obtained image using

        ```bash
        $ docker images
        ```

## II. Networking
Before starting, we need to select a master and number the workers. Then, make sure everyone can ping each other.

We will use `docker overlay network` to connect multiple Docker daemon hosts. `docker swarm` is a tool to manage the network.

Go to root of the git repo.

1. On manager:

    ```bash
    $ docker system prune
    $ master/init_swarm.sh
    ```

    `swarm` initialization will give a message like this

    ```log
    init swarm with master ip: 192.168.31.108
    Swarm initialized: current node (qm53z9bzt6at9hpx19p20jcpz) is now a manager.
    ```

    To add a worker to this swarm, run the following command:

    ```bash
    $ docker swarm join --token SWMTKN-1-5rcl051g8q8y6hpo4vryzhe6p704gcpjfp1at7jg11vg5zu4oo-7k9fcb4o4ggsshyqnmn9t6dxw 192.168.31.108:2377
    ```

    To add a manager to this swarm, run and follow the instructions:

    ```bash
    $ docker swarm join-token manager
    ```

    The token and ip should be shared to the workers in the following step:

    On manager, create an attachable overlay network called `hadoop-net`:

    ```bash
    $ master/init_network.sh
    ```

    You may use the following to check network status:

    ```bash
    $ docker network ls
    ```


2. On `worker-n`, join the swarm.

    ```bash
    $ docker system prune
    ```
    And then paste the command generated in manager. For example,

    ```bash
    $ worker/join_swarm.sh SWMTKN-1-5rcl051g8q8y6hpo4vryzhe6p704gcpjfp1at7jg11vg5zu4oo-7k9fcb4o4ggsshyqnmn9t6dxw 192.168.31.108
    ```

    Use the following to check node status on manager:

    ```bash
    $ docker node ls
    ```

    Result:

    ```log
    ID                            HOSTNAME        STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
    qm53z9bzt6at9hpx19p20jcpz *   hadoop-master   Ready     Active         Leader           20.10.7
    z1ol1zwbxt53j1n79ixhgguw5     ubuntu          Ready     Active                          20.10.7
    ```

## III. Start services

1. Start `hadoop-master` on master machine.

    ```bash
    $ export WORKER_NUMBER=N
    $ master/start.sh
    ```

    or with `sudo`:

    ```bash
    sudo -E master/start.sh
    ```

2. On `worker-n`, start a detached (-d) and interactive (-it) container `hadoop-worker-n` that connects to `hadoop-net`.

    ```bash
    $ export WORKER_NUMBER=N
    $ export WORKER_ID=X
    $ worker/start.sh
    ```
    or with sudo:

    ```bash
    $ sudo -E worker/start.sh
    ```

    *Tip: Check your images and containers:*

    ```bash
    $ docker images
    $ docker ps -a
    ```

    Your container should be in `up` status.

    Check your swarm network connection. `docker network ls` should show `hadoop-net` on worker; in worker container, you should be able to ping master.

3. Start `NameNode` daemon, `DataNode` daemon, `ResourceManager` daemon and `NodeManager` daemon in `hadoop-master` container.

    ```bash
    $ master/start_hadoop.sh
    ```

    Check `jps` to see if the services have been started.

    Run sample task:
    ```bash
    $ ./run-wordcount.sh
    ```

## IV. Drill

1. Check the status of drillbits.

2. Go to `$DRILL_HOME` on master. Run `bin/drill-conf`. If it works fine, you may check the connection of drillbits. Example:

    ```sql
    apache drill> SELECT * FROM sys.drillbits;
    ```

    ```log
    +-----------------+-----------+--------------+-----------+-----------+---------+---------+--------+
    |    hostname     | user_port | control_port | data_port | http_port | current | version | state  |
    +-----------------+-----------+--------------+-----------+-----------+---------+---------+--------+
    | hadoop-master   | 31010     | 31011        | 31012     | 8047      | false   | 1.18.0  | ONLINE |
    | hadoop-worker-1 | 31010     | 31011        | 31012     | 8047      | true    | 1.18.0  | ONLINE |
    +-----------------+-----------+--------------+-----------+-----------+---------+---------+--------+
    2 rows selected (4.515 seconds)

    ```

## Trouble shooting

1. If worker cannot join swarm, and

    ```bash
    $ telnet <ip-of-manager> 2377
    ```
    cannot be reached, then the port 2377 might haven been blocked on manager. Possible solution:

    ```bash
    $ ufw allow 2377
    ```
    Also, the overlay network needs the following ports to open:

    ```bash
    $ ufw allow 7946
    $ ufw allow 4789
    ```

2. Check drillbit status: go to `bin`

    ```bash
    $ ./drillbit.sh status
    ```

    If drillbit is not running, check `log` to see the error. If it says memeory not enough, then you need to edit `conf/drill-env.sh` to appropriate memory. Then restart drillbit.

    ```bash
    $ ./drillbit.sh restart
    ```

3. Drill: Error like

    ```log
    ERROR o.a.c.framework.imps.EnsembleTracker - Invalid config event received {server.1=10.190.3.170:2888:3888:participant, version=0, server.3=10.190.3.91:2888:3888:participant, server.2=10.190.3.172:2888:3888:participant}
    ```

    This is because of zookeeper version update (>3.6.5). Go to `$ZOOKEEPER_HOME/conf/zoo.cfg` and change every

    ```log
    server.0=hadoop-master:2888:3888
    server.1=hadoop-worker-1:2888:3888
    ...
    ```

    to

    ```log
    server.0=hadoop-master:2888:3888;2181
    server.1=hadoop-worker-1:2888:3888;2181
    ...
    ```

    Then restart zookeeper.

    ```bash
    $ $ZOOKEEPER_HOME/bin/zkServer.sh restart
    ```
