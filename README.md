# Kafka Docker Environment

## Clone the git repositoy

     $ git clone https://github.com/rancavil/kafka.git
     $ cd kafka

## Building the image

     $ docker build -t kafka:2.6.0 .

## Executing 

Running Kafka environment as a daemon.

     $ docker run -d --name <container-name> -p 9092:9092 --hostname <your-hostname/ip address> kafka:2.6.0

If you want to know what's happend inside the container, execute the following command.

     $ docker logs -f <container-name>

 
