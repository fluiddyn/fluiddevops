from __future__ import print_function

import os
import subprocess
import configparser
import hggit


def _run(cmd):
    print(cmd)
    cmd = cmd.split()
    subprocess.call(cmd)


def clone(src, dest=None):
    _run('hg clone {} {}'.format(src, dest))


def set_remote(dest, src):
    path = os.path.join(src, '.hg', 'hgrc')
    config = configparser.ConfigParser()
    config.read(path)
    if 'git' in dest:
        dest = 'git+' + dest

    config.set('paths', 'github', dest)
    if not config.has_section('extensions'):
        config.add_section('extensions')

    config.set('extensions', 'hgext.bookmarks', '')
    path_hggit = os.path.dirname(hggit.__file__)
    config.set('extensions', 'hggit', '')
    with open(path, 'w') as configfile:
        config.write(configfile)

    os.chdir(src)
    subprocess.call(['hg', 'paths'])
    os.chdir('..')


def pull(src, dest, update=True):
    os.chdir(dest)
    cmd = 'hg pull ' + src
    if update:
        cmd += ' -u'

    _run(cmd)
    os.chdir('..')


def push(dest, src):
    os.chdir(src)
    print(src)
    _run('hg bookmark -r default master')
    _run('hg push github')
    os.chdir('..')
