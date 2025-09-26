import multiprocessing

bind = '0.0.0.0:8000'
reload = True
reolad_extra_files = [
    'person/templates/person/index.html',
    'article/templates/article/'
]

accesslog = '-'
errorlog = '-'

workers = 1
capture_output = True

timeout = 1800
graceful_timeout = 10

worker_class = 'gthread'
threads = 8 * multiprocessing.cpu_count()

