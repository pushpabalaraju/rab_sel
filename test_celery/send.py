# enabling connection with RabbitMQ

import pika
import sys

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