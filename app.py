from time import sleep
from json import dumps
from kafka import KafkaProducer
import sys
import os


bootstrap_tmp = print(os.environ.get(bootstrap))
boot = str(bootstrap_tmp)
port = ':9092'
boot_strap = boot + port
print(boot_strap)

#producer = KafkaProducer(bootstrap_servers=['b-2.mskworkshopcluster.k2a9xo.c2.kafka.us-west-2.amazonaws.com'],
producer = KafkaProducer(bootstrap_servers=boot_strap, \
value_serializer=lambda x: dumps(x).encode('utf-8'))

for e in range(10000):
    data = {'number' : e}
    producer.send('my-topic', value=data)
    producer.flush()
    sleep(1)
