#!/usr/bin/env python

import argparse
import logging
import sys

from jinja2 import Environment, PackageLoader

from enchy_admin.post.link import Link


jinja2_env = Environment(loader=PackageLoader('enchy_admin', 'templates'))

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format=(
        "[%(asctime)s] %(levelname)s "
        "[%(name)s.%(funcName)s:%(lineno)d] %(message)s"
    ),
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def build_parser():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(
        dest="action", help='actions'
    )

    post_link_parser = subparsers.add_parser(
        'post_link', help='post link'
    )

    return parser


def main():
    parser = build_parser()
    params, other_params = parser.parse_known_args()

    if params.action == "post_link":
        link = Link(
            title=input("Title: "),
            link=input("Link: "),
            description=input("Description: "),
            thumbnail=input("Thumbnail: "),
            template=jinja2_env.get_template('link.rst')
        )
    else:
        print(parser.print_help())

if __name__ == "__main__":
    main()
