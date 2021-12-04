import multiprocessing

command = '/home/tryoha/django/bin/gunicorn'
pythonpath = '/home/tryoha/django/project/'
bind = '127.0.0.1:8882'
# workers = 4
workers = multiprocessing.cpu_count()
user = 1000
group = 1000
