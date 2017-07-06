#!/bin/bash
fluidmirror clone
fluidmirror set-remote

crontab -l 2> backup.cron
echo "*/5 * * * * cd $PWD && source $VIRTUAL_ENV/bin/activate && `which fluidmirror` -c $PWD/mirror.cfg sync" | crontab -
