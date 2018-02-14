"""
fork basics: start 5 copies of this program running in parallel with
the original; each copy counts up to 5 on the same stdout stream--forks
copys process memory, including file descriptors; for doesn't currently
work on Windows without Cygwin: use os.spawnv or multiprocessing on
Windows instead; spawn is roughly like fork+exec combination;
"""

import os, time


def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), i))


for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Process %d spawned' % pid)
    else:
        counter(5)
        os._exit(0)

print('Main process exiting.')
