#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import uuid

def insert_card(type_dict, card):
    if card.get("title"):
        if card.get("is") == "goal":
            description = ", ".join(card.get("keepers", []))
        else:
            description = card.get("description")
        type_dict[f"type-{uuid.uuid4()}"] = dict(
            kind = card.get("is"),
            title = card.get('title'),
            description = description,
        )

def find_card_deck(o):
    if isinstance(o, list):
        for x in o:
            candidate = find_card_deck(x)
            if candidate:
                return candidate
    elif isinstance(o, dict):
        if o.get("type") == "cardDeck":
            return o

def find_card_type_dict(o):
    if isinstance(o, list):
        for x in o:
            candidate = find_card_type_dict(x)
            if candidate:
                return candidate
    elif isinstance(o, dict):
        if "cardTypes" in o:
            return o["cardTypes"]
        else:
            for x in o.values():
                candidate = find_card_type_dict(x)
                if candidate:
                    return candidate 
    else:
        return None

deck = json.load(open('deck-simplified.json'))
template = json.load(open('widgets.json.template'))
card_deck = find_card_deck(template)
card_type_dict = find_card_type_dict(card_deck)
card_type_dict.clear()

initial_cards = card_deck.copy()
initial_cards["id"] = f"{uuid.uuid4()}"

initial_cards['cardTypes'] = dict()
insert_card(initial_cards['cardTypes'], deck['cards'][0])

for card in deck['cards'][1:]:
    insert_card(card_type_dict, card)

card_template_position = 0
while (len(template) > card_template_position and
    template[card_template_position].get("type") != "card"):
    card_template_position += 1

card_template = template.pop(card_template_position)
first_card = True
def card_instance(x):
    global first_card
    card = card_template.copy()
    card["id"] = f"{uuid.uuid4()}"
    card["cardType"] = x
    return card

starting_card_offset_x = 0
starting_card_offset_y = 220

def starting_card(x):
    global starting_card_offset_x
    global starting_card_offset_y
    card = card_template.copy()
    card["deck"] = initial_cards["id"]
    card["id"] = f"{uuid.uuid4()}"
    card["cardType"] = x
    card["faceup"] = True
    card["x"] = (card.get("x", 0)) + starting_card_offset_x
    card["y"] = (card.get("y", 0)) + starting_card_offset_y
    starting_card_offset_x = starting_card_offset_x + 200
    return card

template.append(initial_cards)
template.extend(card_instance(x) for x in card_type_dict.keys())
template.extend(starting_card(x) for x in initial_cards['cardTypes'].keys())

with open("widgets.json", "w") as out:
    json.dump(template, out)