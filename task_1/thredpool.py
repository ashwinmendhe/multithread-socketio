import threading
from concurrent.futures import ThreadPoolExecutor
from random import random

def file_task(i):
    value = random()
    filepath = f'out_{i+1}.txt'
    # sleep(i)
    file = open(filepath, 'w')
    file.write(f'Thread got random value as {value}. \n')

with ThreadPoolExecutor(max_workers=5) as ex:
    
    result = ex.map(file_task,[i for i in range(5)])
    print(threading.active_count())