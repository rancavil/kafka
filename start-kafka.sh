#!/bin/bash

if [ ! -z "$KAFKA_ADVERTISED_LISTENERS" ]; then
	echo "configuring advertised_listener : $KAFKA_ADVERTISED_LISTENERS"
	printf "\nadvertised.listeners=$KAFKA_ADVERTISED_LISTENERS\n" >> $KAFKA_HOME/config/server.properties
fi

echo "starting kafka"
$KAFKA_HOME/bin/kafka-server-start.sh $KAFKA_HOME/config/server.properties
