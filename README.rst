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

- ``python -m fluiddevops.info`` or ``fluidinfo`` to get information on
  currently installed FluidDyn packages.

::
     $ fluidinfo
     Package                 Installed               Version                 Local Path              Remote Path             
     =======                 =========               =======                 ==========              ===========             
     fluiddyn                True                    0.1.4                   /home/avmo...a/fluiddyn ssh://hg@b...n/fluiddyn 
     fluidsim                True                    0.0.0b3                 /home/avmo...a/fluidsim ssh://hg@b...n/fluidsim 
     fluidlab                False                                                                                           
     fluidimage              True                    0.0.2                   /home/avmo...fluidimage ssh://hg@b...fluidimage 
     fluidfft                False                                                                                           
     fluidcoriolis           False                                                                                           
     fluiddevops             True                    0.0.0b3                 /home/avmo...luiddevops ssh://hg@b...luiddevops 
     numpy                   True                    1.13.1                  /usr/lib/p...ages/numpy                         
     cython                  True                    0.26.1                  /usr/lib/p...e-packages                         
     mpi4py                  True                    2.0.0                   /scratch/a...ges/mpi4py                         
     pythran                 False                                                                                           
     pyfftw                  True                    0.10.3.dev0+e827cb5     /scratch/a...egg/pyfftw                         
     matplotlib              True                    2.1.0rc1                /scratch/a...matplotlib                         
     scipy                   True                    0.19.1                  /usr/lib/p...ages/scipy                         
     skimage                 True                    0.13.0                  /scratch/a...es/skimage                         
