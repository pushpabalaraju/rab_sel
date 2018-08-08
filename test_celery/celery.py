from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
             broker='amqp://pushpa:push123@localhost/pushpa_vhost',
             backend='rpc://',
             include=['test_celery.invoice','test_celery.receive'])