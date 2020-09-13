# Background
This kafka-python add is intened to be used with the AWS Workshop for the Managed Sreaming for Kafka (MSK) service.
https://amazonmsk-labs.workshop.aws/en/

The intended purpose of this is to show both a producer and consumer using Python, and to see messages being read dynamically via the Python REPL.

This repository provides links to a container, along with a basic Python script which acts as a 'producer' which generates 10000 messages to a kafka topic. The kafka cluster and brokers hosting the topic are created during the inital MSK workshop steps using either the AWS CLI or the AWS Console.

The container has the python script, required kafka-python libraries and the per-account variables (bootstrap servers and topic name). The container can be launched into the MSK VPC, and associated subnet easily using AWS Fargate.

# Steps
1) Launch MSK (kafka) cluster using the console or CLI (ref:)
2) 
