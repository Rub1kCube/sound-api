import multiprocessing

from sound.asgi import UvicornWorker

bind = '0.0.0.0:5000'
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = UvicornWorker
