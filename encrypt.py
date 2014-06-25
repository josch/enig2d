#!/usr/bin/python
# coding=utf8

import sys

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', u'ä', u'ö', u'ü', ' ']

def encrypt(string, x, y):
    if len(string) % 2 is not 0:
        string+=" "

    string = string.decode("utf8")

    char1 = [i for i in string[0:-1:2].lower()]
    char2 = [i for i in string[1::2].lower()]

    chars_x = [i for i in chars]
    chars_y = [i for i in chars]

    move_x = int(x)
    move_y = int(y)

    for i in xrange(move_x):
        chars_x.insert(0, chars_x.pop())
    for i in xrange(move_y):
        chars_y.insert(0, chars_y.pop())

    print "%03d %03d"%(move_x, move_y),

    for i in xrange(len(char1)):
        print "%03d"%(chars_x.index(char1[i])+len(chars_x)*(chars_y.index(char2[i]))+len(chars_x)+1),

encrypt(' '.join(sys.argv[3:]), sys.argv[1], sys.argv[2])
