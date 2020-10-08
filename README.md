# Background
This kafka-python 'add-on' intened to be used with the AWS Workshop for the Managed Sreaming for Kafka (MSK) service.
https://amazonmsk-labs.workshop.aws/en/

The purpose of this is to show both a producer and consumer using Python, and to see messages being read dynamically via the Python REPL.

This repository provides links to a container, along with a basic Python script which acts as a 'producer' which generates 10000 messages to a kafka topic. The kafka cluster and brokers hosting the topic are created during the inital MSK workshop steps using either the AWS CLI or the AWS Console.

### Output from Kafka-Python container
![0](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/10.png  "Output from producer")

The container has the python script, required kafka-python libraries and the per-account variables (bootstrap servers and topic name). The container can be launched into the MSK VPC, and associated subnet easily using AWS Fargate.

# Option 1
## Read and Write Messages using Kafka CLI Utility
You can follow these steps after the [Amazon MSK Labs > Cluster Creation Lab](https://amazonmsk-labs.workshop.aws/en/clustercreation/console.html#and-off-we-go) section is complete.

If you followed the service creation steps outlined in the lab workshop, you would have a Cloud9 instance created in your account, which is also in the VPC that connects to the MSK service via ENI's in the relevant subnets.

Connect to the Cloud9 instance (called MSKClient-Cloud9EC2Bastion) and open two terminal tabs. One will be for the producer sending the messages, and the other will be for the consumer reading these messages sent to the topic. On the first tab, ssh to the instance created by CloudFormation named 'MSKClient-KafkaClientInstance1' or similar.

### The producer
Once connected to the client instance in your account via ssh, type the following command to begin a 'real-time' channel to send messages to a topic.
Its best to open a terminal tab from within the Cloud9 IDE for your producer, and a seperate terminal tab for your consumer.

Run this from the directory named after your kafka deployemnt. I used used Kafka 2.3.1, so this is the 'kafka231' directory. Bootstrap information for you cluster can be [found](https://docs.aws.amazon.com/msk/latest/developerguide/msk-get-bootstrap-brokers.html) from the AWS console, or via API call.

```bin/kafka-console-producer.sh --topic <Your Topic Name> --broker-list <Your Bootstrap Server FQDN:9092>```

This will open an interactive terminal that allows you to type characters to the topic noted above.

### The consumer
From the Cloud9 terminal tab, navigate to the appropriate kafka directory linked to your release version (directory 'kafka231' in my case) run the following code to read the messages from the producer terminal opened above..

```bin/kafka-console-consumer.sh --topic <Your Topic Name> --bootstrap-server <Your Bootstrap Server FQDN:9092>```



# Option 2
## Read and Write Messages with Python using AWS Fargate

## Step 1) 
### Create AWS MSK 
Following the CloudFormation or CLI as noted in the [Workshop guide](https://amazonmsk-labs.workshop.aws/en/)

## Step 2) 
### Create ECS [cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html) for the container that will run the kafka-python producer code.
![2](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/1a.png  "Step 2")

## Step 3) 
### Select ECS cluster settings
![3](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/1b.png  "Step 3")

## Step 4) 
### Select ECS cluster networking configuration and name, then create
![4](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/2a.png  "Step 4")

## Step 5)
### Create container definition
![5](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/3.png  "Step 5")

## Step 6)
### Select AWS Fargate as 'launch type'
![6](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/4.png  "Step 6")

## Step 7)
### Next we will configure the container details
![7](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/5.png  "Step 7")
Give your task a name, and select the 'ecsTaskExecutionRole' role.

## Step 8)
### Configure the container image, script and environment variable for your MSK cluster
![8](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/6.png  "Step 8")

* Allocate 1Gb of memory and 0.5 CPU - then select 'Add Container'

## Step 9)
### Next we will configure the container details
![9](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/7.png  "Step 9")

* Note: the image container path being pointed to on DockerHub. This could also be hosted on ECR or other container registries.

## Step 10)
### Set Environment Variable 
![10](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/8.png  "Step 10")

### Environment Variable
We set the environment variable for the container we will be lauching with AWS Fargate. The reason for this is to customise the
'bootstrap' variable to point to relevant endpoint name for your MSK cluster.
Enter the first [boostrap server endpoint](https://docs.aws.amazon.com/msk/latest/developerguide/msk-get-bootstrap-brokers.html) name here, which can be found from the AWS console.

### Bootstrap format for Plaintext
xxx.kafka.us-west-2.amazonaws.com:9092 - when adding this variable **exclude** the trailing port number 

## Run task in your MSK VPC and public subnet.

* Once the container is launched using AWS Fargate, you will see messages appear in the consumer window terminal window. This consumer session was created from Cloud9 intance to the MSK Client in your VPC.
* Adjust the security groups for you container to allow access to MSK
![11](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/9.png  "Step 11")

