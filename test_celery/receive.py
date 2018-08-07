from __future__ import absolute_import
from test_celery.celery import app
import time
import pika
import time


@app.task
def recv():
	
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))  #enable connection. 
																						#host=localhost if producer/consumer
																						#on same server/machine
	channel = connection.channel()


	channel.queue_declare(queue='Q1')		#define Queue name
	channel.queue_declare(queue='Q2')
	channel.queue_declare(queue='Q3')


	def call(ch, method, properties, body):		#to print the contents on screen
	    print(" [x] Received %r" % body)
	    time.sleep(body.count(b'.'))
	    print(" [x] Done")
	    ch.basic_ack(delivery_tag = method.delivery_tag)

	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(call,
	                      queue='Q1')

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()
	connection.close()