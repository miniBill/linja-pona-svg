#!/usr/bin/env nix-shell
#! nix-shell -i bash -p pango -p graphicsmagick
set -e
mkdir -p output
chronic pango-view --output="$2" --font="Linja Pona" -q --text "$1"
chronic npx svgo --multipass --pretty -p2 "$2"
