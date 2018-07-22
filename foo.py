#!/usr/bin/python
"""
Python script skeleton.
"""
import sys
import argparse

def main():
    # ------ Parse arguments ------- #
    '''
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument('first_arg')
    parser.add_argument('--three', nargs=3)
    parser.add_argument('--optional', nargs='?')
    parser.add_argument('--all', nargs='*', dest='all')
    parser.add_argument('--one-or-more', nargs='+')

    args = parser.parse_args()

    print(args)
    print(args.first_arg)
    '''
    # ------------------------------ #
    print('Start your code here.')

    l = [1,2,3]
    print l
    print 'new thing i added'
    print 'next new thing'

if __name__ == "__main__":
    sys.exit(main())
