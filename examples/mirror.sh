#!/bin/bash
fluidmirror clone
fluidmirror set-remote

crontab -l 2>/dev/null; echo "*/5 * * * * cd $VIRTUAL_ENV/bin && source activate && fluidmirror -c $PWD/mirror.cfg pull && fluidmirror -c $PWD/mirror.cfg push" | crontab -
