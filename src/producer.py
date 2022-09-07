#!/usr/bin/env python

import pika


class Publisher:
    """ Class publisher """

    def __init__(self, config):
        self.config = config

    def publish(self, routing_key, message):
        connection = self.create_connection()

        # Create a new channel with the next available channel number or pass in a channel number to use
        channel = connection.channel()

        # Creates an exchange if it does not already exist, and if the exchange exists,
        # verifies that it is of the correct and expected class.

        # Publishes message to the exchange with the given routing key
        channel.exchange_declare(
            exchange=self.config['exchange'], exchange_type='topic')
        channel.basic_publish(
            exchange=self.config['exchange'], routing_key=routing_key, body=message)

        print(" [x] Sent message % r for % r" % (message, routing_key))

    def create_connection(self):
        """Create new connection"""
        param = pika.ConnectionParameters(
            host=self.config['host'], port=self.config['port'])
        return pika.BlockingConnection(param)


if __name__ == '__main__':
    publisher_config = {'host': 'localhost',
                        'port': 5672, 'exchange': 'my_exchange'}
    publisher = Publisher(publisher_config)
    publisher.publish('nse.nifty', 'New Data')
