#!/usr/bin/env python
'''Python script to run `fluidmirror sync` intermittently

Usage
-----
nohup python -u mirror_launch.py > ~/.fluiddyn/mirror.log &

'''
from __future__ import print_function

import sched
import time
from datetime import datetime
from random import random
from fluiddevops.mirror import main


s = sched.scheduler(time.time, time.sleep)
every = 15 * 60  # seconds


def job():
    main(['sync'])


print('fluidmirror sync will run every {} seconds'.format(every))
while True:
    print('Time: ', datetime.fromtimestamp(time.time()))
    rnd_delay = random() * 20
    s.enter(every + rnd_delay, 1, job, ())
    s.run()
