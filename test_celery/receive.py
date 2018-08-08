from __future__ import absolute_import
from test_celery.celery import app
import time
import pika
import time

@app.task
def send_p():
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='Q1')
	channel.queue_declare(queue='Q2')
	message1 = "Rabbit eats carrot on Q1"
	message2 = "Rabbit eats carrot on Q2"
	channel.basic_publish(exchange='',                           #
	                      routing_key='Q1',                      # queue name
	                      body=message1,               			 # content to be sent
	                      properties=pika.BasicProperties(
	                         delivery_mode = 2))                   #message is made persistent here
	channel.basic_publish(exchange='',                           #
	                      routing_key='Q2',                      # queue name
	                      body=message2,               			 # content to be sent
	                      properties=pika.BasicProperties(
	                         delivery_mode = 2))                   #message is made persistent here
	print(" [x] Sent 'the text to be printed'")
	connection.close()

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
	    return body

	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(call,
	                      queue='Q1')

	print(' [*] Waiting for messages. To exit press CTRL+C')

	channel.start_consuming()
	bb=call()
	connection.close()
	return bb


@app.task
def recv2():
	
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
	                      queue='Q2')

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()
	connection.close()