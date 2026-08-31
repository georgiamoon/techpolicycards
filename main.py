#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import collections
import json
import os.path
from jinja2 import Environment, FileSystemLoader, select_autoescape

parser = argparse.ArgumentParser(
    prog="TechPolicyCards",
    description="Generates HTML and other exports of the Tech Policy Card Game")

parser.add_argument('-o', '--output', help="Output filename")
parser.add_argument('-t', '--template', help="Template", default='printout.html')
parser.add_argument('--template-directory', help="Template directory", default=os.path.join(os.path.dirname(__file__), 'templates'))
parser.add_argument('-d', '--deck', help="Deck file - defines what cards are in the game", default=os.path.join(os.path.dirname(__file__), 'deck.json'))

subparsers = parser.add_subparsers(dest = 'subparser_name')

list_templates = subparsers.add_parser("list-templates")

report = subparsers.add_parser("report")

args = parser.parse_args()

args.output = args.output or args.template

env = Environment(
    loader = FileSystemLoader(args.template_directory),
    autoescape = select_autoescape(['html', 'xml']),
    trim_blocks=True,
    lstrip_blocks=True)

with open(args.deck) as deck_file:
    deck = json.load(deck_file)


if args.subparser_name == 'list-templates':
    print('\n'.join(env.list_templates()))
elif args.subparser_name == 'report':
    counts = collections.Counter(c.get('is') for c in deck.get('cards', []))
    print('\n'.join(f"{k}: {v}" for (k, v) in counts.items()))
else:
    template = env.get_template(args.template)
    with open(args.output, "w") as result:
        result.write(template.render(deck))
