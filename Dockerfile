FROM ubuntu:18.04

RUN apt update -y && \
    apt install vim -y && \
    apt install wget -y

WORKDIR /home/kafka

RUN wget -q https://downloads.apache.org/kafka/2.6.0/kafka_2.13-2.6.0.tgz && tar zxvf kafka_2.13-2.6.0.tgz && rm kafka_2.13-2.6.0.tgz

RUN apt install openjdk-11-jdk -y

WORKDIR /home/kafka/kafka_2.13-2.6.0

RUN apt-get install supervisor -y

ENV KAFKA_HOME /home/kafka/kafka_2.13-2.6.0
COPY start-kafka.sh $KAFKA_HOME/bin
COPY start-zookeeper.sh $KAFKA_HOME/bin
COPY kafka.conf /etc/supervisor/conf.d/
COPY zookeeper.conf /etc/supervisor/conf.d/

EXPOSE 9092-9094 2181
CMD ["supervisord","-n"]
