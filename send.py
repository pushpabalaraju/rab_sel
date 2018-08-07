from __future__ import absolute_import
from test_celery.celery import app
import time

# enabling connection with RabbitMQ

import pika
import sys


# @app.task
def send_p():
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	for i in range(20):
		channel.queue_declare(queue='Q1')
		message1 = "{}) Rabbit eats carrot on Q1 ".format(i)
		channel.basic_publish(exchange='',                           #
		                      routing_key='Q1',                      # queue name
		                      body=message1)              			 # content to be sent                  #message is made persistent here
	for i in range(20):
		# print("q2")
		channel.queue_declare(queue='Q2')
		message2 = "{}) Rabbit eats carrot on Q2".format(i)
		channel.basic_publish(exchange='',                           #
		                      routing_key='Q2',                      # queue name
		                      body=message2)               			 # content to be sent
	print(" [x] Sent 'the text to be printed'")
	connection.close()