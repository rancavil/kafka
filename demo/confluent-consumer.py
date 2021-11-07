#!/usr/bin/env python
"""
 To use confluent-python:
    python -m pip install confluent-kafka
"""


from confluent_kafka import Consumer, KafkaError


settings = {
        "bootstrap.servers": "localhost:9092",
        "group.id": "tempgroup",
        "client.id": "client-1",
        "enable.auto.commit": True,
        "session.timeout.ms": 6000,
        "default.topic.config": {"auto.offset.reset":"smallest"}
}

c = Consumer(settings)

c.subscribe(["stream-temp"])

try:
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print(f"Received: {msg.value().decode('utf-8')}")
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print(f"End of Partition reached {msg.topic()}/{msg.partition()}")
        else:
            print(f"Error occured: {msg.error().str()}")
except KeyboardInterrupt:
    pass
finally:
    c.close()
