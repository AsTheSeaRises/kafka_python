# Background
This kafka-python 'add-on' intened to be used with the AWS Workshop for the Managed Sreaming for Kafka (MSK) service.
https://amazonmsk-labs.workshop.aws/en/

The purpose of this is to show both a producer and consumer using Python, and to see messages being read dynamically via the Python REPL.

This repository provides links to a container, along with a basic Python script which acts as a 'producer' which generates 10000 messages to a kafka topic. The kafka cluster and brokers hosting the topic are created during the inital MSK workshop steps using either the AWS CLI or the AWS Console.

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

```bin/kafka-console-producer.sh --topic <Your Topic Name> --broker-list <Your Bootstrap Server FQDN:90902>```

This will open an interactive terminal that allows you to type characters to the topic noted above.

### The consumer
From the Cloud9 terminal tab, navigate to the appropriate kafka directory linked to your release version (directory 'kafka231' in my case) run the following code to read the messages from the producer terminal opened above..

```bin/kafka-console-consumer.sh --topic <Your Topic Name> --bootstrap-server <Your Bootstrap Server FQDN:90902>```



# Option 2
## Read and Write Messages with Python using AWS Fargate
Step 1) Create AWS MSK following the CloudFormation or CLI as noted in the [Workshop guide](https://amazonmsk-labs.workshop.aws/en/)

Step 2) Create ECS [cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html) for the container that will run the kafka-python producer code.
![1](https://github.com/AsTheSeaRises/kafka_python/blob/master/images/1a.png  "Step 1")

