#!/usr/bin/env python

def gc_content(dna_str):
    gc = 0
    char = 0
    for letter in dna_str:
        if letter in ['A', 'C', 'G', 'T']:
            char += 1
        if letter in ['G', 'C']:
            gc += 1
    content = (float(gc)/char) * 100
    return content