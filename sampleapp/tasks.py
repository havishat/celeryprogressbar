# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task, current_task
from numpy import random
from scipy.fftpack import fft
import time


@shared_task
def add(x, y):
    time.sleep(5)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@shared_task
def getnames(f, l):
    print('Hello, World!')
    print(f)
    print(l)
    time.sleep(10)
    return f + " " + l

@shared_task
def fft_random(n):
    for i in range(n):
        x = random.normal(0,0.1,2000)
        y = fft(x)
        if(i%30 == 0):
            process_percent = int(100 * float(i) / float(n))
            current_task.update_state(state= 'PROGRESS',
                                    meta= {'process_percent': process_percent})
    return random.random()

@shared_task
def add1(x,y):
    for i in range(10000000):
        a = x + y
    return x+y
