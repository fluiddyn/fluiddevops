#!/usr/bin/env python
'''Python script to run `fluidmirror sync` intermittently

Usage
-----
nohup python -u mirror_launch.py > ~/.fluiddyn/mirror.log 2>&1 &

'''
from __future__ import print_function

import sched
import time
from datetime import datetime
from random import random
from fluiddevops.mirror import main


s = sched.scheduler(time.time, time.sleep)
every = 60 * 60  # seconds


def job():
    print('fluidmirror sync will run every {} seconds'.format(every))
    while True:
        print('Time: ', datetime.fromtimestamp(time.time()))
        rnd_delay = random() * 20
        s.enter(every + rnd_delay, 1, main, [['sync']])
        s.run()


if __name__ == '__main__':
    job()
