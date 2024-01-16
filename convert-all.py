#!/usr/bin/env python
import subprocess

with open("input/needed.txt") as needed:
    for line in needed:
        subprocess.call(["./convert.sh" ,line ])
