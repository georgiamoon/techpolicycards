#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
        loader = FileSystemLoader("templates/"),
        autoescape = select_autoescape(['html', 'xml']))

deck = json.load(open('deck.json'))
template = env.get_template('printout.html')
with open("printout.html", "w") as result:
    result.write(template.render(deck).encode('utf-8'))
