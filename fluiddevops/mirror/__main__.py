import argparse
import os
from .config import read_config, get_repos
from .vcs import clone, pull, push, set_remote


def parse_args():
    parser = argparse.ArgumentParser(prog='fluidmirror')
    parser.add_argument(
        '-c', '--cfg', help='config file', default='mirror.cfg')
    subparsers = parser.add_subparsers(help='sub-command')

    parser_list = subparsers.add_parser(
        'list', help='list all configured repositories')
    parser_list.set_defaults(func=_list)

    parser_clone = subparsers.add_parser(
        'clone', help='clone all repositories based on config')
    parser_clone.set_defaults(func=_clone_all)

    parser_setr = subparsers.add_parser(
        'set-remote', help='set remote path in hgrc of all configured repositories')
    parser_setr.set_defaults(func=_setr_all)

    parser_pull = subparsers.add_parser(
        'pull', help='pull all configured repositories')
    parser_pull.set_defaults(func=_pull_all)

    parser_pull = subparsers.add_parser(
        'push', help='push all configured repositories')
    parser_pull.set_defaults(func=_push_all)

    return parser.parse_args()


def _list(args):
    read_config(args.cfg, output=True)


def _all(func, args, key='pull'):
    config = read_config(args.cfg)
    os.chdir(os.path.dirname(args.cfg))
    for repo in get_repos(config.sections()):
        func(config['repo:' + repo][key], repo)


_clone_all = lambda args: _all(clone, args)
_setr_all = lambda args: _all(set_remote, args, 'push')
_pull_all = lambda args: _all(pull, args)
_push_all = lambda args: _all(push, args, 'push')


args = parse_args()
args.func(args)
