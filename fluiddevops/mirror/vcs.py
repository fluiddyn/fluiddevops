from __future__ import print_function

import os
import subprocess
import configparser


def _run(cmd, output=False):
    print(cmd)
    cmd = cmd.split()
    if output:
        return subprocess.check_output(cmd)
    else:
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
    config.set('extensions', 'hggit', '')
    with open(path, 'w') as configfile:
        config.write(configfile)

    os.chdir(src)
    subprocess.call(['hg', 'paths'])
    os.chdir('..')


def pull(src, dest, update=True, output=False):
    os.chdir(dest)
    cmd = 'hg pull ' + src
    if update:
        cmd += ' -u'

    output = _run(cmd, output)
    os.chdir('..')
    return output


def push(dest, src):
    os.chdir(src)
    print(src)
    _run('hg bookmark -r default master')
    _run('hg push github')
    os.chdir('..')


def sync(src, pull_repo, push_repo):
    output = pull(pull_repo, src, output=True)
    if all([string not in output for string in ['no changes', 'abort']]):
        push(push_repo, src)
