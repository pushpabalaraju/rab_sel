from __future__ import absolute_import
from test_celery.celery import app
import time
import pika
import time


@app.task
def read():
	print("im reading")

@app.task
def extract():
	print( 'extracted')	

@app.task
def classify():
	print( 'classified')

@app.task
def sign():
	print('signed and completed')
	