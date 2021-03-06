import os.path as path
from multiprocessing import Pool
import time
from logging import Handler

def process_file(name):
    ''' Process one file: count number of lines and words '''
    linecount=0
    wordcount=0
    with open(name, 'r') as inp:
        for line in inp:
            linecount+=1
            wordcount+=len(line.split(' '))

    return name, linecount, wordcount

def process_files_parallel(arg, dirname, names):
    ''' Process each file in parallel via Poll.map() '''
    pool=Pool()
    results=pool.map(process_file, [path.join(dirname, name) for name in names])
    return results

def process_files(arg, dirname, names):
    ''' Process each file in via map() '''
    results=map(process_file, [path.join(dirname, name) for name in names])
    return results

if __name__ == '__main__':
    start=time.time()
    path.walk('input/', process_files, None)
    print("process_files()", time.time()-start)

    start=time.time()
    path.walk('input/', process_files_parallel, None)
    print("process_files_parallel()", time.time()-start)