# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:43:57 2019

@author: johns
"""

a = 1
b = 2
if a < b:
    print 'a is less than b'
    print 'a is definetrly less than b'
print 'Not sure if a is less than b'


c = 3
d = 4
if c < d:
    print 'c is less than d'
else:
    print 'c is NOT less than d'
    print "I don't rhink c is less than d"
print 'outside the if block'

e = 10
f = 8
if e < f:
    print 'e is less than f'
elif e == f:
    print 'e es equal to f'
elif e > f + 10:
    print 'e is greater than f by more than 10'
else:
    print 'e is not less than f'
    
g = 9
h = 8
if g < h:
    print 'g is less than h'
else:
    if g == h:
        print 'g is equal to h'
    else:
        print 'g is greater than h'