#!/bin/env python3


filepath = "list.txt"
with open(filepath) as fp:
    lines = fp.read().splitlines()
with open(filepath, "w") as fp:
    for line in lines[30::]:
        print(line + " : 'blocklist_de_bruteforce'", file=fp)
