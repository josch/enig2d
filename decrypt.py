#!/usr/bin/python
# coding=utf8

import sys

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', u'ä', u'ö', u'ü', ' ']

def decrypt(string):
    list = u"".join(string).split(' ')

    chars_x = [i for i in chars]

    chars_y = [i for i in chars]

    move_x = int(list[0])
    move_y = int(list[1])

    for i in xrange(move_x):
        chars_x.insert(0, chars_x.pop())
    for i in xrange(move_y):
        chars_y.insert(0, chars_y.pop())

    output = ""

    for num in [int(i) for i in list[2:]]:
        output+="%s%s"%(chars_x[(num-len(chars))%len(chars)-1], chars_y[int((num-len(chars)-1)/len(chars))])

    print output

decrypt(sys.argv[1:])
