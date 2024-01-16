#!/usr/bin/env nix-shell
#! nix-shell -i bash -p pango -p graphicsmagick
pango-view --output="output/$1.svg" --font="Linja Pona" -q --text "$1"
npx svgo --multipass --pretty -p2 "output/$1.svg"
