# Tech Policy Cards

A card game, inspired by [Fluxx](https://www.looneylabs.com/games/fluxx), i.e. a game where the rules and win conditions change as you play the cards in your hand (just like life!).
This game is developed around the concepts of internet health and on the issues and policies that we see in tech policy. 

Check out the current cards in the [deck](https://techpolicy.cards/printout.html), which you can print and cut out at home.

Check out the [repo on Github](https://github.com/georgiamoon/techpolicycards). Contribute to the [game](https://techpolicy.cards/CONTRIBUTING).

## Basic Play

- Everyone starts with 3 cards
- Initial play is  Draw 1, Play 1; 1 Goal to start.
- Anyone can join at any time

## Card Structure

- **Rules (Policy changes that affect the state of play)**
  - Title
  - Sub-title
  - Description
- **Keepers (Characters/Actors/ Items that are needed to achieve Goals)**
  - Name
  - Category
- **Actions (events that occur in one play round, can affect anyone in the game or the person playing the Action)**
  - Title
  - Description
- **Goals (How to win the game, usually requires some combination of Keepers to be held by the player)**
  - Name
  - Keepers to achieve goal

## Resources

- Card Template: [https://boardgamegeek.com/filepage/107967/fluxx-custom-card-template](https://boardgamegeek.com/filepage/107967/fluxx-custom-card-template)
- Fluxx Vanilla Card Set: [https://www.looneylabs.com/lists/fluxx-card-list](https://www.looneylabs.com/lists/fluxx-card-list)

## Creating & Editing Cards 

1) Edit `deck.json` to add cards.  Find an existing card of the type you want ("is": "keeper" for a keeper, etc), copy it, and change the words for your idea.
2) Run `render.py`. There are some dependencies, running via `uv run render.py` will make sure they are available. Add `--help` to see options.
3) Print the `printout.html`.

Current cards in the [printout](https://techpolicy.cards/printout.html).

## Playing Online

Creates a save file that can be imported to the website [playingcards.io](https://playingcards.io).

1) Run `render-pcio.py`.
2) The script outputs `widgets.json`.
3) Create a `zip` of `widgets.json` and upload to [playingcards.io](https://playingcards.io).


## Contributors:

- David Winslow ([@dwins](http://github.com/dwins))
- OTI ([@opentechinstitute](http://github.com/opentechinstitute))
  - Ross Schulman ([@rschulman](http://github.com/rschulman))
  - Chris Ritzo ([@critzo](http://github.com/critzo))
  - Nat ([@natmey](http://github.com/natmey))
  - Sharon, Tiffany, Jo, Alison, ...more...
- Players at [MozFest]([http://mozillafestival.org])
- Meag Doherty ([@meagdoh](https://github.com/meagdoh))
- Jack Aponte ([@jackaponte](http://github.com/jackaponte))
- JaimeV
- Helyx Chase
- Maya Wagoner ([@mayawagon](http://github.com/mayawagon))
- Kim Garcia
- [@kaythaney](https://github.com/kaythaney)
- [@riordan](https://github.com/riordan)
- Stephen Soltesz ([@stephen-soltesz](http://github.com/stephen-soltesz))
- Simone Basso ([@bassosimone](https://github.com/bassosimone))
- Roberto D'Auria ([@evfirerob](https://github.com/evfirerob))
- kinkade ([@kinkade](https://github.com/nkinkade))
- oktacon 4.0 attendees
- [@elioqoshi](https://github.com/elioqoshi) & [@uracreative](https://github.com/uracreative)
- [Global Gathering](https://www.globalgathering.community/) 2026
- Digital Rights Game Creators
