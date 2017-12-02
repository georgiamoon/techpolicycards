#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
        loader = FileSystemLoader("templates/"),
        autoescape = select_autoescape(['html', 'xml']))

deck = json.load(open('deck-poster.json'))
template = env.get_template('poster.html')
with open("poster.html", "w") as result:
    result.write(template.render(deck).encode('utf-8'))
