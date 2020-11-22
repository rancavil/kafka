# Kafka Docker Environment

## Clone the git repositoy

     $ git clone https://github.com/rancavil/kafka.git
     $ cd kafka

## Building the image

     $ docker build -t kafka:2.6.0 .

## Executing 

Running Kafka environment as a daemon.

     $ docker run -d --name <container-name> -p 9092:9092 --hostname <your-hostname/ip address> kafka:2.6.0

If you want to know what's happen inside the container, execute the following command.

     $ docker logs -f <container-name>

## Testing

Verifiying if container is running.

     $ docker ps

We can use the following example to verify if Kafka is working. We are going to use a **python** and their **kafka module**. We will write a consumer and a producer.

The producer will send messages to topic (called topic_1) and the consumer will read from.

Installing python kafka module.

     $ pip install kafka-python

Writing **producer.py**

     #!/usr/bin/env python

     import kafka as k
     import time

     if __name__ == '__main__':
         producer = k.KafkaProducer(bootstrap_servers=['<hostname/ip address>:9092'])
         print('Sending Data')
         for i in range(1,101):
             print('Sendind Data {}'.format(i))
             producer.send('topic_1',b'Hey this is data {}'.format(i))
             time.sleep(1)
     producer.flush()

Writing **consumer.py**

     #!/usr/bin/env python

     import kafka as k

     if __name__ == '__main__':
         consumer = k.KafkaConsumer('topic_1',bootstrap_servers=['<hostname/ip address>:9092'])
         for msg in consumer:
             print (msg.value)

**Important:** you must set up <hostname/ip address>. If you are in a local environment you can use **localhost**
