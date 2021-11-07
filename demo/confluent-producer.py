#!/usr/bin/env python
"""
 To use confluent-python:
    python -m pip install confluent-kafka
"""


from random import randint
from confluent_kafka import Producer


def acked(err, msg):
    if err is not None:
        print(
            f"Failed to deliver message : {msg.value().decode('utf-8')} : {err.str()}"
        )
    else:
        print(f"Message produced: {msg.value().decode('utf-8')}")

p = Producer({"bootstrap.servers":"localhost:9092"})


try:
    for _ in range(100):
        temp = randint(1,30)
        p.produce(
            "stream-temp", key="temp", value=f"{temp}degrees",
            callback=acked
        )
        p.poll(0.5)
except KeyboardInterrupt:
    pass

p.flush(30)
