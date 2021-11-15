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
        print (msg.value.decode("utf-8"))
