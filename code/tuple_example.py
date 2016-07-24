#!/usr/bin/env python

import sys

def minmax(items):
    return min(items), max(items)

def main(items):
    print (minmax(items))

if __name__ == '__main__':
    main(sys.argv[1])
