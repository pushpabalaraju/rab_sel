import time
from test_celery.celery import app

@app.task
def invoicing():
	print("Invoicing process completed")
	# print(x)
	