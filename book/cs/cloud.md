# Cloud

* computing resources are provisioned in a shareable way so that users get what they need when they need
* Best be defined as infrastructure as a service or IaaS
* Keep their data secure, accessible, and available
* Operate in lots of different geographic regions → easily duplicate your data across multiple sites

* Cloud computing
  * platform independent → increase mobility and productivity
  * more storage capacity

* Pros
  * Cheap : Pay as you go, free tier
  * Scalability : dynamically increasing instances (Pokemon go)
  * Data safety : Backing up data across the globe in different data center
  * Extensibility : Built in monitoring, machine learning, block chain solution

> Term

* On-prem
  * servieces of the business runs from within the confines of the organization
  * data stays in its own private network
  * [+] security : prevents potential data breach
  * [+] customization : unique solutions catering to their needs
  * [+] vendor lock-in : cost of switching to a differnt vendor is high (i-tunes)

* Serverless
  * No servers involved when running the service to remove infrastructure administration
  * Faas is a way to implmenet serverless

* Service account
  * special kind of account used by an application or a VM instance
  * make authorized API calles
  * identified by its email address, w/o passwords, and cannot log in via browsers / cookies
  * associated with private/public RSA key-pairs that are used for authentication to Google
  * You can let other users or service accounts impersonate a service account

> Cloud

* Hybrid Cloud
  * Sensitive in public, secure in private

* Multi cloud
  * [-] Increase in complexity

* Private Cloud
  * used by a single large corporation and generally physically hosted on its own premises

* Public Cloud
  * large cluster of machines run by another company

> Service

![cloud services](images/20210307_183109.png)

* IaaS (Infrastructure as a service)
  * You shouldn't have to worry about building your own network or your own servers
  * AWS, GCP, Azure

* PaaS (Platform as a service)
  * abstracts away the server instances you need
  * subset of cloud computing where a platform is provided for customers to run their services
  * execution engine is provided for whatever software someone wants to run
  * web developer writing a application w/o entire server complete with file system, dedicated resources
  * AWS Elastic Beanstalk, Google app engine, Heroku

* SaaS (Software as a service)
  * way of licensing the use of software to others while keeping that software centrally hosted and managed
  * [-] has to share it's data with service provider, limit to the customization flexibility (ex. fix service down, high latency)
  * Google workspace, dropbox, salesforce

* FaaS (Function as a Service)
  * Event driven service model, only triggered when an event occurs (HTTP, web request)
  * [+] Batch job, cron job
  * [+] Easy to scale : stateless processes (image compression, video analysis)
  * [-] Cold start problem : depends on service provider, environment configuration, memory footprint
  * [-] Complexity : overall project becomes complex
  * Amazon's AWS lambda, Google Cloud function


## Docker

![alt](images/20210215_121636.png)

* Carves up a computer into sealed containers that run your code
* Written in go managing kernels

> Install

* Automatic
  *kcurl -s https://get.docker.com/ | sudo sh

* Maunal
  * curl -fsSL https://get.docker.com -o get-docker.sh
  * chmod +x get-docker.sh
  * ./get-docker.sh

* Allow Sudo
  * sudo usermod -aG docker $USER
  * sudo reboot

```sh
sudo vi /etc/systemd/system/docker.service.d/http-proxy.conf
# [Service]
Environment="HTTP_PROXY=http://proxy.example.com:80/"
```

* image defined by your Dockerfile should generate containers that are as ephemeral as possible
* Sort multi-line arguments.
* Always combine RUN apt-get update with apt-get install

> Terms

* Channel
  * Test channel : pre-releases that are ready for testing before general availability (GA).
  * Stable channel : latest releases for general availability (<year>.<month>)
  * Nightly channel : latest builds of work in progress for the next major release.

* .dockerignore
  * used to build better Docker images. avoid uploading unnecessary files reducing build time /image size

* bridges

![alt](images/20210216_201500.png)

```sh
apt-get update && apt-get install bridge-utils

docker run -ti --rm -v --net=host ubuntu:16.04 bash
docker network create new # add one more to list

# terminal
apt update && apt install brid install bridge-utils
brctl list
```

* bridges
  * uses NAT and bridges to create virtual Ethernet networks

* container
  * Self-contained sealed unit of software → contains everything required to run the code
  * code / configs / process / network / dependencies / operating system
  * ephemaral: exit when process that started it exits (have its own IP address)
  * dependent on images and use them to construct a run-time environment and run an application
  * contents of layers are moved between containers in gzip files
  * [-] filesystem isn't designed for high I/O

* image
  * every file that makes up just enough of the operating system to do what you need to do
  * Image ID is Internal docker representation of image

* kernel
  * uses cgroups to contain processes
  * uses namespaces to contain networks
  * copy-on-write filesystems to build images

* ns
  * allow processes to be attached to private network segments
  * private networks are bridged into shared network with rest of containers
  * containers haver virtual network cards
  * containers get their own copy of networking stack

* Repository
  * Where it came from

* registry
  stores layers and images, listen on port 5000
  maintains index and searches tags, authorize authentication

* route

```sh
docker run -ti --rm --net=host --privileged=true ubuntu bash
docker run -ti -p 8080:8080 ubuntu bash # will add port forwarding in iptables

# in docker 1
apt-get update && apt-get install iptables
iptables -n -L -t nat
```

* socket
  * By default, a unix domain socket (or IPC socket) is created at /var/run/docker.sock, requiring either root permission, or docker group membership.

* Stroage
  * Block : Fixed size of data, no metadata is stored, I/O intensive apps, store persistent application data
  * Object : metadata + unique identifier, scalability is limitless, accessed with HTTP calls, store images (aws S3)

* Storage driver
  * control how images, container are stored in docker host (overlay2)

* tag
  * maybe empty → better to refer it by IMAGE ID
  * Version number

* Hypervisor
  * Hyperkit(OSX) / hyper-V (Win) (direct link to infrastructure)
  * VirtualBox / VMWare (run on host OS)

* Volume
  * recommended way to persist data, `/var/lib/docker/volumnes/`

> Error

* Error response from daemon: removal of container <containerid> is already in progress
  * restart docker

* "-v": executable file not found in $PATH: unknown.
  * image argument must come last (-v page:page image:latest)
  * docker run -ti image:latest bash -v page:page

* Hang when apt [Connecting to archive.ubuntu.com (91.189.88.142)]
  * use apt-get update

* docker: Error response from daemon: driver failed programming external connectivity on endpoint
  app_2 (d408c39433627b00183bb): Bind for 0.0.0.0:80 failed: port is already allocated.
  * A port can be assigned to only one container/process at a time

```sh
docker run -d -p 80:3000 --name app_1 app
# 06fbad4394aefeb45ad2fda6007b0cdb1caf15856a2c800fb9c002dba7304896
docker run -d -p 80:3000 --name app_2 app
# d5e3959defa0d4571de304d6b09498567da8a6a38ac6247adb96911a302172c8
```

* Cannot download images: Error response from daemon: unauthorized: authentication requried.
  * docker login (registry)

* ERROR COPY `book` /note/book not found
  * check if `book` is in gitignore

### Dockerfile

* small program to create an image
* Each line takes image from previous and make another image → append changes at the end
* process you start on one line will not be running next line → use ENV

> Tip: General

* Sort multi-line arguments
* absolute minimum set up and configuration
* can be piped useful to perform one-off builds without writing a Dockerfile
* echo -e 'FROM busybox\nRUN echo "hello world"' | docker build -
* Reducing size of your final image
  * order them from the less frequently changed
  * instructions RUN, COPY, ADD create layers

> Command

* ADD
  * local_path docker_path (copy local_path to docker_path)
  * Copy file, if compressed, decompress automatically (depends on OS)
  * If file is from URL, use permission 600 and doesn’t decompress
  * root:root by default
  * project.com/download/1.0/project.rpm : project

* ARG [name][=[default value]]
  * defines a variable that users can pass at build-time to the builder (--build-arg [varname]=[value])

* CMD ["executable","param1","param2"] (exec) / command param1 param2 (shell)
  * provide defaults for an executing container
  * run once when container has started, using docker run     # can override using run IMG CMD
  * does not execute anything at build time, but specifies the intended command for the image.
  * Must be used once, if multiple used last

* COPY [--chown=[user]:[group]] `src`... `dest`
  * copies files or directories from `src`, adds them to the filesystem of the container at the path `dest`
  * may contain wildcards and matching will be done using Go’s filepath.Match rules
  * Doesn’t change file permission

{% tabs %}
{% tab title='Dockerfile' %}

```dockerfile
FROM httpd:2.4
COPY "$PWD" /usr/local/apache2/htdocs/
# Without Dockerfile
# docker run -dit --name container_name -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4 && \
# docker exec -it container_name bash

# With Dockerfile
# docker build --pull --rm -f "Dockerfile" -t image_name:latest "." && \
# docker run --rm -it -p 8080:80 --name container_name image_name:latest bash
```

{% endtab %}
{% tab title='index.html' %}

```html
<h1>Run in docker</h1>
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title='install_sudo.Dockerfile' %}

```sh
FROM ubuntu:latest
RUN apt-get update && apt-get -y install sudo
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
USER docker
```

{% endtab %}
{% endtabs %}

* FROM : [required]
  * `image` : set base image

{% tabs %}
{% tab title='multistage.Dockerfile' %}

```sh
FROM ubuntu:16.04 as builder
RUN apt-get update
RUN apt-get -y install curl
RUN curl https://google.com | wc -c > google_size

FROM alpine
COPY --from=builder /google_size /google_size
ENTRYPOINT echo google is this big; cat google_size

docker build -t google_size .
docker images                 # google_size is only 5.57MB
```

{% endtab %}
{% endtabs %}

* ENV
  * environment for all subsequent instructions in the build stage and can be replaced inline
  * View using docker inspect, and change them using docker run --env `<key>=<value>`
  * Environment variable persistence can cause unexpected side effects
  * $VAR ${VAR} ${VAR:-DEFAULT}
  * docker run --e : override this option

* ENTRYPOINT command param1 param2
  * allows you to configure a container that will run as an executable
  * start of the commands to run (arguments CAN NOT be over-ridden)
  * ENTRYPOINT will be started as a subcommand of /bin/sh -c, which does not pass signals.
  * Only the last ENTRYPOINT instruction in the Dockerfile will have an effect

* EXPOSE 80/udp
  * informs Docker that the container listens on the specified network ports at runtime
  * TCP or UDP, and the default is TCP
  * docker run -P flag to publish all exposed ports and map them to high-order ports
  * Sample backend

{% tabs %}
{% tab title='hello.Dockerfile' %}

```sh
# docker run imagename echo hello
cat Dockerfile
FROM ubuntu
CMD ["echo"]
```

{% endtab %}
{% tab title='flask.Dockerfile' %}

```sh
FROM python:3.8

ARG GIT
ARG OAUTH
ARG SERVICE_ACCOUNT
ARG PORT=8080
ARG TEST=false

ENV PORT=${PORT} \
  PYTHONPATH=/page \
  GIT=${GIT} \
  OAUTH=${OAUTH} \
  SERVICE_ACCOUNT=${SERVICE_ACCOUNT}

COPY requirements.txt /
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
  sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
  apt-get -y update && \
  apt-get install -y google-chrome-stable vim && \
  pip install -r requirements.txt
COPY page/ /page
RUN python -m page.test;
RUN [ "$TEST" = true ] || python -m page.setup;

CMD gunicorn --bind :$PORT --workers 1 --threads 12 "page.app:create_app()";
```

{% endtab %}
{% tab title='data.js' %}

```js
module.exports = {
  DB: 'mongodb://mongo:27017/mydb'
}
```

{% endtab %}
{% tab title='index.js' %}

```js
import express from 'express';
import mongodb from 'mongodb';
import config from './data';

const app = express();
const PORT = 4000;
const client = mongodb.MongoClient;

client.connect(config.DB, { useNewUrlParser: true }, (err, db) => {
  if(err) {
    console.log('database is not connected')
  }
  else {
    console.log('connected!!')
  }
});

app.get('/', (req, res) => {
  res.json("I love docker!");
});

app.listen(PORT, () => {
  console.log('Your server is running on PORT:',PORT);
});
```

{% endtab %}
{% tab title='package.json' %}

```json
{
  "name": "backend",
  "version": "1.0.0",
  "description": "Simple node and express backend",
  "main": "index.js",
  "repository": "github:mannyhenri/node-docker",
  "scripts": {
    "start": "nodemon ./index.js --exec babel-node -e js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.16.3",
    "mongodb": "^3.1.6",
    "nodemon": "^1.18.4"
  },
  "devDependencies": {
    "babel-cli": "^6.26.0",
    "babel-preset-env": "^1.7.0",
    "babel-preset-stage-0": "^6.24.1"
  }
}
```

{% endtab %}
{% endtabs %}

* LABEL : adds metadata to an image

* RUN ["executable","param1", ..] (exec) / command param1 .. (shell)
  * /bin/sh -c on Linux or cmd /S /C
  * execute in a new layer on image and commit results → used for the next step in the Dockerfile
  * parsed as JSON, which means that you must use double-quotes + escape backslashes
  * cache for RUN instructions can be invalidated by docker build --no-cache.

* USER
  * `user` : set user (default root)

* VOLUME
  * avoid defining shared folders in Dockerfiles

* workdir
  * cd before all other command

### Docker-machine

* when your Host OS does not support running Docker Engine natively
* docker-machine env-default

> CLI

* env : Get environment variable
* ip default : Get default IP
* start
* create
* restart

### Docker-compose

> Error

* docker-compose cannot use gcloud credential helper on Linux

```sh
docker logout
docker login

gcloud auth activate-service-account --key-file=[키 파일]
gcloud auth configure-docker
```

> Docker-compose

* Compose file provides document, configure application’s dependencies (db, queues, caches, web API)
* Simple machine coordination → kubernetes for larger

* build
  * --no-cache : Do not use cache when building the image.
* down : kill existing
* exec
  * db psql postgres postgres
* up : Create and start containers (build + run)
  * -d : Run containers in the background, print new container names.
  * --force-recreate : Recreate containers even if their configuration and image haven't changed.
  * --build : Build images before starting containers.
* ps : lists all the containers for services mentioned in the current yml
* stop : stops running containers of specified services in yml file.
* help : display
* images : lists images built using the current docker-compose file
* version : check if installed
* logs container : prints all the logs created by all services if not specified

* run
  * creates containers from images built for services in yml. runs a specific service provided as an argument
  * -v volume_name:/path : start container with volume

* build : builds services in yml (skip if service is using prebuilt image)
  * -f FILE : Specify an alternate compose file (default: docker-compose.yml)
  * -p NAME : Specify an alternate project name (default: directory name)
  * --verbose : Show more output

> docker-compose.yml

* manage multiple Dockerfile

* version: "3.6" : specification for backward compatibility but is only informative

* services (/services)
  * blkio_config : defines a set of configuration options to set block IO limits for this service
  * dns : defines custom DNS servers
  * command : overrides default command declared by the container image (CMD)
  * cpu_count : number of usable CPUs for service container
  * cpu_shares : service container relative int CPU weight versus other containers
  * cpu_period : allow Compose implementations to configure CPU CFS (Completely Fair Scheduler) period when platform is based on Linux kernel
  * cpu_quota : allow Compose implementations to configure CPU CFS (Completely Fair Scheduler) quota when platform is based on Linux kernel
  * cpu_percent : usable percentage of the available CPUs.
  * mac_address :
  * image : set default image (node:lts)
  * env_file : adds environment variables to the container based on file content
  * entrypoint : overrides default entrypoint for the Docker
  * environment : environment have precedence over env_file
  * expose : must expose from container, must be accessible to linked services

* deploy (/services/sid/deploy)
  * mode : replicated (default), global
  * labels : com.example.description: "description"
  * replicas : replicas specifies # containers that SHOULD be running at any given time.
  * resources : physical constraints for container to run on platform (limits, reservations)
  * preferences: : platform's node SHOULD fulfill, datacenter: us-east
  * restart_policy : condition, delay

* build (/services/sid/build)
  * context : path to a directory containing a Dockerfile or url to a git repository
  * dockerfile : alternative dockerfile webapp.Dockerfile
  * args : can be omitted, build arg won't be set if not set by command building image
  * labels : add metadata to the resulting image
  * shm_size : size of the shared memory (/dev/shm)
  * target : defines the stage to build as defined inside a multi-stage

* networks (/services/sid/networks)
  * aliases : aliases declares alternative hostnames for this service on network
  * priority: 1000 : set numeric priority of network
  * ipv4/6_address : static IP address for containers for this service when joining network

{% tabs %}
{% tab title='volumes.yaml' %}

```yml
ports:
  - "3000" /  "3000-3005" /  "8000:8000" / "9090-9091:8080-8081"
  - "127.0.0.1:8001:8001" / "127.0.0.1:5000-5010:5000-5010" / "6060:6060/udp"
```

{% endtab %}
{% tab title='volumes.yaml' %}

```yml
services:
  backend:
  image: awesome/database
  volumes:
    - db-data:/etc/data
  backup:
  image: backup-service
  volumes:
    - db-data:/var/lib/backup/data

volumes:
  db-data:
```

{% endtab %}
{% endtabs %}

### Docker CLI

![alt](images/20210216_195648.png)

* build
  * docker_dir : build folder with Dockerfile
  * --rm : Remove intermediate containers after a successful build
  * --pull : Always attempt to pull a newer version of the image
  * -t tag . : tag name to

* cp : copy from / to container
  * */ : copy direcrtory

* events : get real-time events from the server
* info : Display system-wide information

* history image_id
  * Show the history of an image

> container

* prune -f
* stop registry : stop registry
* rm -v registry : remove registry
* cat /proc/self/cgroup | head -1 | tr --delete ‘10:memory:/docker/’ : Get full docker inside docker

* attach
  * container-name : links a local input, output, and error stream to a container

* cp
  * foo.txt mycontainer:/foo.txt : One file can be copied TO the container like
  * mycontainer:/foo.txt foo.txt : One file can be copied FROM the container like

* detach
  * ctrl + p, ctrl + q → detach and continue running

* start
  * container : start container
  * -a : attach STDOUT / STDERR and forward signals
  * -i : attach container’s STDIN

* stop
  * name : stop container

* exec
  * starts another process in an existing container → good for debugging and DB administration / can't add ports, volumns
  * -it : interactive mode
  * jenkins cat /var/jenkins_home/secrets/initialAdminPassword : Get password

* commit
  * container_id  IMAGE:TAG : convert container to images return image_id
  * -m "commit messages"

* tag
  * image new_id : Change image to new_id
  * image_id docker_id/alpine:tag1 : tag images (seanhwangg.io/page connect to remote)

* cp
  * container:path host_path

* diff
  * see changes from created image

* kill
  * container : change to stop state

* load

* mount
  * Muse use exact file path on the host -> volumne

* rm
  * <container_name> : remove container
  * -f : Force remove
  * $(docker ps -a -q) : remove all containers

{% tabs %}
{% tab title='cleanup.sh' %}

```sh
#!/bin/bash
docker ps -q | xargs docker inspect --format='{{ .State.Pid }}' | xargs -IZ sudo fstrim /proc/Z/root/
docker rm -v $(docker ps -a -q -f status=exited)
docker rmi $(docker images -f "dangling=true" -q)
du -h
```

{% endtab %}
{% endtabs %}

* Network
  * port
  * container : List port mappings or a specific mapping for the container

{% tabs %}
{% tab title='echo_server.sh' %}

```sh
docker run -it -p 2345 -p 2346 --name echo-server ubuntu:14.04 bash
docker port echo-server # in other terminal
# 2345/tcp -> 0.0.0.0:49158
# 2346/tcp -> 0.0.0.0:49157
```

{% endtab %}
{% endtabs %}

* network
  * use host if no isolation is needed
  * docker network create learning
  * ls : list of all
  * create nw : create nw
  * rm / prune : Remove one or more networks / all unused networks
  * connect image nw

{% tabs %}
{% tab title='communicate' %}

```sh
# Terminal 1
docker run --rm -ti --net learning --name catserver ubuntu:14.04 bash
nc -lp 1234
ping dogserver

# Terminal 2
docker run --rm -ti --net learning --name dogserver ubuntu:14.04 bash
nc catserver 1234
```

{% endtab %}
{% endtabs %}

* login
  * -u / -p : user pw

* logout

* ps : display all running container
  * -a : Show all containers
  * -q : Only display numeric IDs
  * -s : Display total file sizes
  * -l / -n -1 : Show the latest (n last) created container
  * --no-trunc : Don’t truncate output

{% tabs %}
{% tab title='format.sh' %}

```sh
--format $FORMAT
export FORMAT="\nID\t{{.ID}}\nIMAGE\t{{.Image}}\nCOMMAND\t{{.Command}}\nCREATED\t{{.RunningFor}}\nSTATUS\t{{.Status}}\nPORTS\t{{.Ports}}\nNAMES\t{{.Names}}\n"
```

{% endtab %}
{% endtabs %}

* pull
  * `HOSTNAME/PROJECT-ID/IMAGE:TAG` : Pull image or a repository from a registry (jenkins /ubuntu)

* push
  * `image` : push `image` to docker

* logs
  * `container` : show output of the `container`

{% tabs %}
{% tab title='logs.sh' %}

```sh
docker run --name log -d ubuntu bash -c "lose /etc/password"
docker logs log   # bash: lose: command not found
```

{% endtab %}
{% endtabs %}

* inspect
  * `image` / `container` : show image, container information
  * volume : Show volume information
  * --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'     # '{{.State.Pid}}'

* history
  * image : show history of image

* image
  * prune -f : remove unused images

* images
  * Display all docker images
  * a : See all container (including stopped container)
  * l : Last container to exit

* rmi
  * image_name : remove image
  * -f : Force remove

{% tabs %}
{% tab title='remove_pattern.sh' %}

```sh
docker images -a | grep "pattern" | awk '{print $3}' | xargs docker rmi
```

{% endtab %}
{% endtabs %}

* run
  * `image` `cmd` : Start an empty new container (latest by default)
  * -d : Run in detached mode
  * -e : set environment variable
  * -ti : Terminal interactive
  * --rm : Delete container after exit
  * --name : set container name
  * --link cont : can see env of container 'aaa'
  * --restart=always : restart policy
  * -v / --volume host:cont : Mount directory within docker (files if file exists)
  * --privileged=true --pid=host : can kill other docker
  * --memory / --cpu-quota / shares : limit cpu and memory

{% tabs %}
{% tab title='hello.sh' %}

```sh
-ti ubuntu bash -c "cat /etc/lsb-release"            # show ubuntu version
--name mongo-db -v /data:/data/db -p 27017:27017     # mongodb
-p 8080:8080 -p 50000:50000 jenkins/jenkins          # bind named volume # slave communication
--rm -v /var/run/docker.sock:/var/run/docker.sock docker sh    # docker in docker
--publish 8080:8080 -v jenkins_home:/var/jenkins_home --name jenkins jenkins/jenkins:lts
```

{% endtab %}
{% tab title='shared.sh' %}

```sh
# terminal 1
docker run -ti --name dog -v /shared ubuntu bash
echo hi > /shared/bosom

# terminal 2
docker run -ti --volumes-from dog ubuntu bash  # go away if all containers exits
ls /shared    # bosom
```

{% endtab %}
{% tab title='link.sh' %}

```sh
# terminal 1
docker run --rm -ti -e SECRET=internet --name catserver ubuntu:14.04 bash
nc -lp 1234
nc dogserver 1234   # getaddrinfo: Name or service not known

# terminal 2
docker run --rm -ti --link catserver --name dogserver ubuntu:14.04 bash
nc catserver 1234   # works
nc -lp 4321

env  # CATSERVER_NAME=/dogserver/catserver, CATSERVER_ENV_SECRET=internet
```

{% endtab %}
{% endtabs %}

* save
  * -o my-images.tar.gz debian:sid busybox ubuntu:14.04

* search
  * `image` : Search Docker Hub for `image`

{% tabs %}
{% tab title='inspect.sh' %}

```sh
sudo systemctl daemon-reload
sudo systemctl show --property Environment docker
sudo systemctl restart docker        # restart docker
```

{% endtab %}
{% endtabs %}

* secret
  * ls : list all secrets
  * rm : rm
  * create name file|item : create secret

* service
  * ls : list all services
  * ps : see detailed service
  * create : create new service

* stats
  * top : ps
  * -a : show only running
  * --no-stream : show once

* system
  * df : information regarding amount of disk space used by docker daemon
  * prune : remove stopped, volumes unused by container, dangling image
  * ls

* top
  * Display the running processes of a container

* version : Show the Docker version information

* volume
  * ls : see all available volumes
  * inspect vid : inspect more about volume id
  * create name : create volume `name`
  * rm name : create volume `name`
  * prune : remove all unused volume

![volume, mount](images/20210305_010431.png)

## Kubernates

![alt](images/20210216_200719.png)

* open-source platform
* designed to automate deploying, scaling, and operating application containers
* Kubernetes Clusters to scale are registration and service discovery

> Install

* docker, virtual box

* mac
  * curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"

> Term

* Controller
  * reliability, scalability, LB
  * ReplicaSets
  * Deployment
    * declarative updates for pods and ReplicaSets
    * pause and resume
  * DaemonSets
    * ensure that all nodes run a copy of specific pod
  * services
    * allow communication between one set of deployments with another
    * to get pods in two deployments to talk to each other
    * Internal : IP is only reachable within the cluster
    * External : endpoint available through node ip:port (called Nodeport)
    * Load balancer : Expose application to the internet with a LB

![pod, replica set, deployment](images/20210320_021628.png)

![services](images/20210320_021947.png)

* Labels
  * key / value pair that are attached to objects like pods services deployments
  * ex : release, stable, canary, dev, qa

* kubelet : Kubernetes node agent that runs on each node

* Kube-proxy
  * process that runs on all worker nodes
  * reflects services as defined on each node
  * Mode
    * user space
    * iptables
    * ipvs

* Master Node
  * Overall management of clusters
  * API Server : front end
  * Scheduler : Creates pods, design pods to run on specific node
  * Controller Manager
    * node controller : worker states
    * replication controller : maintain correct number of pods
    * end-point contoroller : join services, pods together
    * service account and token controller : access management

* Namespace
  * allows teams to access resources with accountability
  * divide cluster resources between users
  * default namespace is created

* Node
  * requirements
    * kubelet running
    * can be physical machine or container tools like docker
    * kube-proxy process running
    * supervisord
  * ex: minikube

* Pods : simplest ephemaral unit that kubernetes can interact with
  * most common use case is to use the single-container-in-a-Pod model
  * create, deploy, delete, represents one running process on your cluster (not necessarily made by Docker)
  * contains one or more docker container, storage resources, unique network ip, run options
  * pending, running, succeeded, failed, CrashLoopBackoff
  * cannot be splited across nodes, they share the same set of resources, and can communicate with each other through localhost

* podspec
  * yaml file that describes a pod

* ReplicaSets
  * Ensure specific number of replics for a pod are running at all times

* Selectors
  * Used with kubectl
  * =, != : equality-based
  * IN, NOTIN, EXISTS

* storage
  * shared resources by podsj

* volume

> pod scheduling

* API server : central component of a Kubernetes cluster running on the master node
  * in minikube both master and worker nodes are baked into the same virtual machine (can be different)
* scheduler : watch for unassigned pods and assign to a node with available CPU and memory matching Pod requirements running on the master node
* Kubelet : make sure that assigned pods are running on the node running on each node

1. Kubernetes client (kubectl) sent a request to the API server requesting creation of a Pod defined in the pod/db.yml file.
2. Since the scheduler is watching the API server for new events, it detected that there is an unassigned Pod
3. The scheduler decided which node to assign the Pod to and sent that information to the API server.
4. Kubelet is also watching the API server. It detected that the Pod was assigned to the node it is running on.
5. Kubelet sent a request to Docker requesting the creation of the containers that form the Pod. In our case, the Pod defines a single container based on the mongo image.
6. Kubelet sent a request to the API server notifying it that the Pod was created successfully.

![pod scheduling sequence with rs](images/20210323_000853.png)

> Service

1. Kubernetes client (kubectl) sent a request to the API server requesting the creation of the Service based on Pods created through the go-demo-2 ReplicaSet.
1. Endpoint controller is watching the API server for new service events. It detected that there is a new Service object.
1. Endpoint controller created endpoint objects with the same name as the Service, and it used Service selector to identify endpoints (in this case the IP and the port of go-demo-2 Pods).
1. kube-proxy is watching for service and endpoint objects. It detected that there is a new Service and a new endpoint object.
1. kube-proxy added iptables rules which capture traffic to the Service port and redirect it to endpoints. For each endpoint object, it adds iptables rule which selects a Pod.
1. The kube-dns add-on is watching for Service. It detected that there is a new service.
1. The kube-dns added db's record to the dns server (skydns).

![sequence after service created](images/20210323_002114.png)

### yml

* apiVersion : [required]
* kind : [required]
  * so that Kubernetes knows what we want to do (create a Pod) and which API version to use
* metadata : provides information that does not influence how the Pod behaves
  * to define the name of the Pod (db) and a few labels
* spec : can have multiple containers defined as a Pod
  * .replicas. sets the desired number of replicas of the Pod (default 1)
  * .containers
    * name : (ex. db)
    * image : (ex. mongo),
    * command : command that should be executed when the container starts (mongod)
    * args : defined as an array with (ex. [--rest, --httpinterface])

{% tabs %}
{% tab title='replica_set.yml' %}

```yml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: go-demo-2
spec:
  replicas: 2
  selector:
    matchLabels:
      type: backend
      service: go-demo-2
  template:
    metadata:
      labels:
        type: backend
        service: go-demo-2
        db: mongo
        language: go
    spec:
      containers:
      - name: db
        image: mongo:3.3
      - name: api
        image: vfarcic/go-demo-2
        env:
        - name: DB
          value: localhost
        livenessProbe:
          httpGet:
            path: /demo/hello
            port: 8080
```

{% endtab %}
{% tab title='hello_world.yml' %}

```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: helloworld
spec:
  selector:
  matchLabels:
    app: helloworld
  replicas: 1 # tells deployment to run 1 pods matching the template
  template: # create pods using pod definition in this template
  metadata:
    labels:
    app: helloworld
  spec:
    containers:
    - name: helloworld
      image: karthequian/helloworld:latest
      ports:
      - containerPort: 80
```

{% endtab %}
{% tab title='cron_job.yml' %}

```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
  spec:
    template:
    spec:
      containers:
      - name: hello
        image: busybox
        args:
        - /bin/sh
        - -c
        - date; echo "Hello, World!"
      restartPolicy: OnFailure
```

{% endtab %}
{% endtabs %}

* create
  * Create a resource from a file or from stdin

```sh
cronjob cron --image=cron --schedule="*/5 * * * *" --dry-run=client -o yaml        # create yaml
-f yaml                # run yaml
```

* delete
  * pod : delete pods
  * nodes / pods / jobs name : delete node

### kompose

* conversion tool to go from Docker Compose to Kubernetes
* convert
  * -c : convert to helm chart

{% tabs %}
{% tab title='install.sh' %}

```sh
# Linux
curl -L https://github.com/kubernetes/kompose/releases/download/v1.22.0/kompose-linux-amd64 -o kompose
# macOS
curl -L https://github.com/kubernetes/kompose/releases/download/v1.22.0/kompose-darwin-amd64 -o kompose
chmod +x kompose
sudo mv ./kompose /usr/local/bin/kompose
```

{% endtab %}
{% endtabs %}

### Helm (Kubernetes package manager)

* a tool for managing Kubernetes packages called charts. Helm can do the following:
  * Create new charts from scratch
  * Package charts into chart archive (tgz) files
  * Interact with chart repositories where charts are stored
  * Install and uninstall charts into an existing Kubernetes cluster
  * Manage the release cycle of charts that have been installed with Helm

> Term

* Chart : bundle of information necessary to create an instance of a Kubernetes application
  * push them to helm repository
* config : contains configuration information that can be merged into a packaged chart to create a releasable object
* release : a running instance of a chart, combined with a specific config.

> Files

* Chart.yaml : A YAML file containing information about the chart
* values.yaml : The default configuration values for this chart
* values.schema.json : OPTIONAL: A JSON Schema for imposing a structure on the values.yaml file
* charts/ : A directory containing any charts upon which this chart depends.
* crds/ : Custom Resource Definitions
* LICENSE : [optional] A plain text file containing the license for the chart
* README.md : [optional] A human-readable README file
* templates/ : A directory of templates that, when combined with values, will generate valid Kubernetes manifest files.
  * templates/NOTES.txt : [optional] A plain text file containing short usage notes

{% tabs %}
{% tab title='chart.yaml' %}

```yml
apiVersion: The chart API version (required)
name: The name of the chart (required)
version: A SemVer 2 version (required)
kubeVersion: A SemVer range of compatible Kubernetes versions (optional)
description: A single-sentence description of this project (optional)
type: The type of the chart (optional)
keywords:
  - A list of keywords about this project (optional)
home: The URL of this projects home page (optional)
sources:
  - A list of URLs to source code for this project (optional)
dependencies: # A list of the chart requirements (optional)
  - name: The name of the chart (nginx)
    version: The version of the chart ("1.2.3")
    repository: (optional) The repository URL ("https://example.com/charts") or alias ("@repo-name")
    condition: (optional) A yaml path that resolves to a boolean, used for enabling/disabling charts (e.g. subchart1.enabled )
    tags: # (optional)
      - Tags can be used to group charts for enabling/disabling together
    import-values: # (optional)
      - ImportValues holds the mapping of source values to parent key to be imported. Each item can be a string or pair of child/parent sublist items.
    alias: (optional) Alias to be used for the chart. Useful when you have to add the same chart multiple times
maintainers: # (optional)
  - name: The maintainers name (required for each maintainer)
    email: The maintainers email (optional for each maintainer)
    url: A URL for the maintainer (optional for each maintainer)
icon: A URL to an SVG or PNG image to be used as an icon (optional).
appVersion: The version of the app that this contains (optional). Needn't be SemVer. Quotes recommended.
deprecated: Whether this chart is deprecated (optional, boolean)
annotations:
  example: A list of annotations keyed by name (optional).
```

{% endtab %}
{% endtabs %}

> CLI

* history `chartname` : show history
* install `chartname`
  * --values=my_values.yaml : value injection into template files
* package
* rollback `chartname` `number` : rollback to number
* search
* upgrade `chartname`

### kubectl (Kubernetes cluster manager)

> Error

* The connection to the server 127.0.0.1:55001 was refused - did you specify the right host or port?
  * minikube start

> CLI

* api-resources
* apply
  * -f https://k8s.io/examples/controllers/nginx-deployment.yaml

* cluster-info

* completion
  * echo 'source <(kubectl completion zsh)' >>~/.zshrc

* config
  * current-context : display current context (ex: minikube)
  * view : Show Merged kubeconfig settings
  * get-context : display list of contexts
  * unset users.foo : delete user foo

* create
  * -f helloworld.yaml : creates a deployment resource from the file helloworld.yaml
  * deployment `app_name` : deploy
    * nginx --image=nginx : start a single instance of nginx
  * secret cloudsql-oauth-credentials
    * --from-file

* delete
  * svc `service` : delete `service`
  * pod `db` : remove pod named `db`
  * -f `file.yml` : delete pod defined in `file.yml` (each container get 30s for the processes in those containers can shut down gracefully)
    * --cascade=false : prevent Kubernetes from removing all the downstream objects

* describe
  * svc `service` : describe `service`

* exec
  * `db` ps aux : check status in pod `db`

* expose
  * deployment `helloworld`
    * --type=NodePort : exposes deployment outside of cluster
  * rs `helloworld`
    * --target-port=28017
    * --type=NodePort : If NodePort is used, ClusterIP will be created automatically

* get
  * all : Display one or many resources (pod is only accessible by its internal IP address within the cluster)
    * deployment : check if the deployment was created
    * --selector env=production
  * componentstatuses
  * nodes : verify minikube and virtualBox are talking each other (ex: minikube Ready 9d v1.19.4)
  * pods : show pods
    * --show-labels : Show labels for all pods
  * rs : show replica set
  * services : List all services in the namespace

* label
  * `pod` app=`label` : create new label
    * --overwrite
  * `app`- : delete `app` label

* port-forward
  * svc/app-service 8000:80

* rollout status deployment/nginx-deployment

* run `db` : create pod named `db`
  * --image `mongo` : run pod `mongo` (BAD)
  * --generator "run-pod/v1"

* service helloworld : open web browser to app that is running in Kubernetes

* version
  * --output=yaml

### minikube

* lightweight kubernetes implementation that creates a VM on local machine
* deploys a simple cluster containing only one node
* contains docker and localkube library and rkt

> CLI

* apply
  * Apply a configuration to a resource by filename or stdin.

* cluster-info
  * dump : detailed information about overall health of cluster

* dashboard
  * --url

* delete

* describe
  * `name` : (ex. cronjob)

* docker-env : (ex : export DOCKER_HOST="tcp://127.0.0.1:55003" ...)
  * eval $(minikube docker-env) : every command we send to our local Docker client will be executed on the Minikube VM

* get
  * -o : output format (yaml)
  * all : see all nodes
  * --watch
  * cronjob / pods : list all cronjob
  * deployments / service : show all deployment / service

* ip

* logs
  * `pod` | TYPE/NAME : see logs inside `pod`

* start : sets up a Kubernetes dev environment for you via VirtualBox.
  * --driver=docker
  * --vm-driver=virtualbox

* status : show minikube type
* ssh : go into ssh

* version
  * --client : client version

* service
  * `app` : access service through web (ex: helloworld)
  * list

## AWS

* [Create Key](https://console.aws.amazon.com/iam/home?region=us-east-2#/users/sean?section=security_credentials)

> Term

* Fargate : automatically manages your containers, providing the correct computational resources to your application

### aws (Amazon Web Service)

* [Install CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)
* configure
  * list

{% tabs %}
{% tab title='~/.aws/config' %}

```txt
[default]
region=us-west-2
output=json
```

{% endtab %}
{% tab title='~/.aws/credentials' %}

```txt
[default]
aws_access_key_id=AKIAUBU4SQ7HQRFTLW6S
aws_secret_access_key=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
```

{% endtab %}
{% endtabs %}

### ecs (Elastic Container Service)

* simplifies building, releasing, and operating production-ready containerized applications on Amazon ECS from a local development environment

> Term

* Cluster: the logical grouping of ECS resources.
* Service: resource that allows you to run and maintain a specified number of instances of a task definition simultaneously, in an Amazon ECS cluster.
* Task-Definition: a text file, in JSON format, that contains all the definitions and configurations of your containers.

> cli

* [Install CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html)
* --version
* configure
  * --cluster test
  * --default-launch-type FARGATE
  * --config-name test
  * --region eu-west-1
* up
  * --cluster-config test
  * --vpc YOUR_VPC_ID
  * --subnets YOUR_SUBNET_ID_1, YOUR_SUBNET_ID_2

## GCP

![alt](images/20210214_175023.png)

* cloud location
  * SEOUL (asia-northeast3)


> Terms

* artifact
* container
* storage
  * Multi regional : frequent access
  * regional : cheap in certain region
  * nearline : infrequent access
  * coldline : long term backup

* OAuth2
  * Allows a user to give permission for an app to act on their behalf
  * Register your app with Google (provide a client id, and client secret)
  * Redirect user to authorization URL (happens on google’s server), Google shows consent screen
  * Google provides an authorization code
  * your app exchanges the code for a token and include token with subsequent requests to Google)

* OIDC
  * Extension to OAuth2 providing features for convenience
  * You register a third-party application as a client to the provider.
  * The client sends a request to the provider’s authorization URL.
  * The provider asks the user to authenticate / consent to the client acting on their behalf.
  * The provider sends the client a unique authorization code
  * The client sends the authorization code back to the provider’s token URL
  * The provider sends the client tokens to use with other URLs on behalf of the user

* Project
  * Name must be longer than 6 character

> How to

* [Enable Billing](https://cloud.google.com/appengine/docs/python/console/#billing)
* [Moitoring](https://console.cloud.google.com/monitoring?project=seannote&timeDomain=1h)


### App engine

![web application](images/20210322_230844.png)
![mobile](images/20210322_230832.png)

### bg (Big Query)

* ls

### gsutil (Goolge Cloud storage)

* defacl
  * Get, set, or change default ACL on buckets
* du
* ls
* cp
  * a.py gs://seansdevnote/ : copy a.py to gs://seansdevnote/
* mb (Make buckets)
  * -b off : uniform bucket-level access setting
* status
  * gsutil version: 4.55
* -m rsync -r ./static gs://[YOUR_GCS_BUCKET]/static

### gcloud (Google Cloud)

![alt](images/20210214_175053.png)

* [Resource manager](https://console.cloud.google.com/cloud-resource-manager)
* [Images](https://console.cloud.google.com/gcr/images/seansdevnote?project=seansdevnote)
* Alpha and beta command groups are not final and may change in the future

> Error

* ERROR: (gcloud.run.deploy) Cloud Run error: Container failed to start. Failed to start and then listen on the port defined by the PORT environment variable. Logs for this revision might contain more information
  * -> doesn't run exec gunicorn

> cli

* --version : show version

* artifacts
  * repositories create quickstart-docker-repo --repository-format=docker --location=us-central1
  * repositories list

* app
  * deploy --project `project_id` : deploy app.yaml

* auth
  * configure-docker : register gcloud as a Docker credential
  * list : Show current active account
  * login : login to auth
  * print-access-token
  * revoke : logout

* builds
  * submit . : deploy defined configuration written in cloud.yaml
  * describe : get information about a particular build
  * --tag gcr.io/seansdevnote/flask-fire : builds docker in server dir
  * --config cloudbuild.yaml : use config file
  * --build-arg request_domain=mydomain

* cheat-sheet : show usefulj

* cloud-shell ssh

* component
  * install `kubectl` : install
  * update : process may take several minutes

* compute
  * instances list : see all instances
  * instances create : create instance

* components
  * install docker-credential-gcr
  * update : update all components

* compute
  * addresses list : list all address

* config : ~/.kube/config
  * configurations list : manage multiple configurations
  * list : show all configuration
  * --kubeconfig=config-demo config unset contexts.gke_seannote_us-central1-a_api : unset contexts
  * set : Set a Cloud SDK property.
    * project : change current project
  * unset : Unset a Cloud SDK property.
  * get-contexts
  * get-value project : get project id
  * set run/platform managed run/region us-central1
  * view : show config in KUBECONFIG=~/.kube/config:~/.kube/kubconfig2

* container
  * get-credentials api
    * --zone us-central1-a
    * --project seannote
  * clusters create api
    * --scopes
    * --num-nodes
    * --zone `us-west1-a`
  * images list : list all images
  * images list-tags gcr.io/seansdevnote/page : list all tags

* delete

* dns
  * record-sets transaction start --zone=MANAGED_ZONE :
  * managed-zones list : show all managed zones

* init : authorize SDK tools to access cloud using credentials, default config
  * --console-only

* info : show commands

* projects
  * create : create new project
  * describe
  * get-iam-policy my_project
    * PROJECT_ID : Show all emails and roles
  * list

* iam
  * service-accounts list : see all service accounts
  * service-accounts keys list --iam-account githubaction@seansdevnote.iam.gserviceaccount.com
* info
  * --show-logs
* run
  * deploy
  * --image gcr.io/seansdevnote/flask-fire : set image
  * services list : show all services
  * services describe name : show result of service

* sql
  * instances describe `instance_id`
  * databases list
  * connect `instance_name`
    * --user postgres

* topic : help command
  * gcloudignore

{% tabs %}
{% tab title='cloudbuild.yaml' %}

```yml
steps:
  - name: "gcr.io/cloud-builders/docker"
    args: ["build", "-t", "gcr.io/my-project/my-image", "."]
    timeout: 500s
  - name: "gcr.io/cloud-builders/docker"
    args: ["push", "gcr.io/my-project/my-image"]
```

{% endtab %}
{% endtabs %}
