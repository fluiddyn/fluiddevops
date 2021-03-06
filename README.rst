===========
FluidDevOps
===========

|release|

.. |release| image:: https://img.shields.io/pypi/v/fluiddevops.svg
   :target: https://pypi.python.org/pypi/fluiddevops/
   :alt: Latest version

FluidDevOps is a small package which provides some console scripts to
make DevOps easier.

See directory ``docker`` for more on running Docker containers.

Installation
------------

::

    python setup.py develop

Features
--------

-  ``python -m fluiddevops.mirror`` or ``fluidmirror`` to setup hg to
   git mirroring for a group of packages and periodically check for
   updates

::

    usage: fluidmirror [-h] [-c CFG] {list,clone,set-remote,pull,push} ...

    positional arguments:
      {list,clone,set-remote,pull,push}
                            sub-command
        list                list all configured repositories
        clone               clone all repositories based on config
        set-remote          set remote path in hgrc of all configured repositories
        pull                pull all configured repositories
        push                push all configured repositories
        sync                sync all configured repositories

    optional arguments:
      -h, --help            show this help message and exit
      -c CFG, --cfg CFG     config file
