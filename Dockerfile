FROM ubuntu:20.04

RUN apt update -y && \
    apt install vim -y && \
    apt install wget -y

RUN apt install openjdk-11-jdk -y && apt install supervisor -y && apt install sudo

WORKDIR /home/kafka

RUN wget -q https://downloads.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz && tar zxvf kafka_2.13-3.0.0.tgz && rm kafka_2.13-3.0.0.tgz

ENV KAFKA_HOME /home/kafka/kafka_2.13-3.0.0
COPY docker-entrypoint.sh /home/kafka
COPY start-kafka.sh $KAFKA_HOME/bin
COPY start-zookeeper.sh $KAFKA_HOME/bin
COPY kafka.conf /etc/supervisor/conf.d/
COPY zookeeper.conf /etc/supervisor/conf.d/

EXPOSE 9092-9094 2181
CMD ["bash","/home/kafka/docker-entrypoint.sh"]
