# FluidDevOps

FluidDevOps is a small package which provides some console tools to make DevOps
easier.

See directory `docker` for more on running Docker containers.

## Installation

```
python setup.py develop
```

## Features

- [x] `fluidmirror` to setup hg to git mirroring

```
usage: fluidmirror [-h] [-c CFG] {list,clone,set-remote,pull,push} ...

positional arguments:
  {list,clone,set-remote,pull,push}
                        sub-command
    list                list all configured repositories
    clone               clone all repositories based on config
    set-remote          set remote path in hgrc of all configured repositories
    pull                pull all configured repositories
    push                push all configured repositories

optional arguments:
  -h, --help            show this help message and exit
  -c CFG, --cfg CFG     config file
```
