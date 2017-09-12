from __future__ import print_function
from importlib import import_module as _import
import os
import shlex
import inspect
from collections import OrderedDict
try:
    import subprocess32 as subprocess
except ImportError:
    import subprocess


COL_WIDTH=32


def _get_hg_repo(path_dir):
    pwd = os.curdir
    os.chdir(path_dir)
    cmd = shlex.split('hg paths')
    output = subprocess.check_output(cmd)
    os.chdir(pwd)
    try:
        output = output.splitlines()[0]
    except:
        pass

    if output == '':
        return 'not an hg repo'
    elif output.startswith('default'):
        return output.split(' ')[2]
    else:
        return output


def make_dict_about(pkg):
    about_pkg = OrderedDict([
        ('installed', None),
        ('version', None),
        ('local path', None),
        ('remote path', None),
    ])
    try:
        pkg = _import(pkg)
    except ImportError:
        about_pkg['installed'] = False
        return about_pkg
    else:
        about_pkg['installed'] = True
        about_pkg['version'] = pkg.__version__
        about_pkg['local path'] = os.path.dirname(
            os.path.dirname(inspect.getsourcefile(pkg)))
        about_pkg['remote path'] = _get_hg_repo(about_pkg['local path'])
        return about_pkg


def get_info():
    pkgs = OrderedDict.fromkeys(
        ['fluiddyn', 'fluidsim', 'fluidlab', 'fluidimage', 'fluidfft',
         'fluidcoriolis', 'fluiddevops', 'fluidsim-scripts', 'fluidkth']
    )
    for pkg in pkgs:
        dict_pkg = make_dict_about(pkg)
        pkgs[pkg] = dict_pkg

    return pkgs

def print_info(pkgs):
    pkgs_keys = list(pkgs)
    title = ['Package']
    title.extend([col.title() for col in pkgs[pkgs_keys[0]]])
    title2 = ['=' * len(col) for col in title]
    def print_item(item):
        print(item.ljust(COL_WIDTH), end='')

    for col in title:
        print_item(col)

    print()
    for col in title2:
        print_item(col)

    print()
    def print_pkg(about_pkg):
        for v in about_pkg.values():
            v = str(v)
            if len(v) > COL_WIDTH:
                v = v[:10] + '...' + v[10 + 4 - COL_WIDTH:]
            print_item(str(v))

        print()

    for pkg_name, about_pkg in pkgs.items():
        print(pkg_name.ljust(COL_WIDTH), end='')
        print_pkg(about_pkg)


def main():
    pkgs = get_info()
    print_info(pkgs)


if __name__ == '__main__':
    main()
