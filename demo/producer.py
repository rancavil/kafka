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
