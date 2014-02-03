#!/usr/bin/env python
#-*- coding: utf-8 -*-

def f(x):
    return x**2

print 'first way: ',f(3)

g = lambda x: x**2
print 'second way: ',g(3)

print 'three way: ', (lambda x: x**2) (3)
