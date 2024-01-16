#!/usr/bin/env python

import fileinput
import os.path
import re
import subprocess

with open("input/needed.txt") as needed:
    lines = [line.rstrip() for line in needed]

lines.sort()

size_regex = re.compile('width="(\\d+)" height="(\\d+)"')

for line in lines:
    replaced = line.replace(" ", "-").replace("+", "-")
    svg_filename = f"output/{replaced}.svg"
    if os.path.isfile(svg_filename):
        with open(svg_filename) as svg:
            header = svg.readline()
            match = size_regex.search(header)

            (width, height) = match.groups()
            width = int(width)
            height = int(height)
    else:
        subprocess.call(["./convert.sh", line, svg_filename])

        for svgline in fileinput.input(svg_filename, inplace=True):
            match = size_regex.search(svgline)
            if match:
                (width, height) = match.groups()
                width = int(width) - 20
                height = int(height) - 20
                print(
                    f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="10 10 {width} {height}">',
                )
            else:
                print(svgline, end="")

    print(
        replaced,
        f'\n<ruby><div style="display:inline-block;background-color:currentColor;width:{width*2}px;height:{height*2}px;mask:url(https://toki-pona-svg.netlify.app/{replaced}.svg)"></div> <rt>{replaced.replace("-"," ")}</rt></ruby>\n',
    )

# <div style="background-color: currentColor; height: 18px; mask: url(http://localhost:8080/output.svg);width: 154px;display: inline-block;"></div>
