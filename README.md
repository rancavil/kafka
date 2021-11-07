# Kafka Docker Environment

## Clone the git repository

     $ git clone https://github.com/rancavil/kafka.git
     $ cd kafka

## Building the image

     $ docker build -t kafka:3.0.0 .

## Executing 

Running Kafka environment as a daemon.

     $ docker run -d --name <container-name> -p 9092:9092 --hostname <your-hostname/ip address> kafka:2.6.0

If you want to know what's happen inside the container, execute the following command.

     $ docker logs -f <container-name>

## Testing

Verifiying if container is running.

     $ docker ps
     CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                                             NAMES
     e44d345e8703        kafka:3.0.0         "supervisord -n"    11 seconds ago      Up 4 seconds        2181/tcp, 9093-9094/tcp, 0.0.0.0:9092->9092/tcp   <container-name>


We can use the following example to verify if Kafka is working. We are going to use a **python** and their **kafka module**. We will write a consumer and a producer.

The producer will send messages to topic (called **topic1**) and the consumer will read from.

You have to install **python kafka module**.

    $ pip install kafka-python

Writing **producer.py**

    #!/usr/bin/env python

    import socket
    import kafka as k


    if __name__ == "__main__":
        hostname = socket.gethostname()
        producer = k.KafkaProducer(
                bootstrap_servers=[f"{hostname}:9092"],
                api_version=(0, 10, 1)
        )
        print("Sending data")
        for i in range(1,101):
            msg = f"Data {i}"
            print(f"Sending {msg}")
            future = producer.send("stream-1",msg.encode("utf-8"))
            result = future.get(timeout=10)

        producer.flush()


Writing **consumer.py**

    #!/usr/bin/env python

    import socket
    import kafka as k

    if __name__ == '__main__':
        hostname = socket.gethostname()
        consumer = k.KafkaConsumer("stream-1",
                bootstrap_servers=[f"{hostname}:9092"],
                api_version=(0, 10, 1)
        )
        print("Receiving Data")
        for msg in consumer:
            print (msg.value)

**Important:** you can set up **<hostname/ip address>**. If you are in a local environment you can use **localhost**

You have to execute:

The **producer**.

     $ python producer.py
     Sending Data
     Sendind Data 1
     Sendind Data 2
     Sendind Data 3
     ....
     ...
     ..

In another terminal the **consumer**.

     $ python consumer.py
     Data 1
     Data 2
     Data 3
     ....
     ...
     ..
   
Another way to test how kafka container is working.

**Creating a topic**

We will create a topic called **TOPIC_TEST**

     $ docker exec -i <container-name> bin/kafka-topics.sh --create --topic TOPIC_TEST --bootstrap-server localhost:9092

**Writing some messages (events)**

We must execute and write messages (events) using the **TOPIC_TEST**

     $ docker exec -i <container-name> bin/kafka-console-producer.sh --topic TOPIC_TEST --bootstrap-server localhost:9092
     >This is an event with data
     >Another event

**Reading messages (events)**

The command executes a kafka consumer and wait for events, reading from **TOPIC_TEST**.

     $ docker exec -i <container-name> bin/kafka-console-consumer.sh --topic TOPIC_TEST --from-beginning --bootstrap-server localhost:9092
     This is an event with data
     Another event
