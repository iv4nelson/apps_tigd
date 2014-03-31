#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import random

list_names = ["ivan","foo","bar","mary","peter"]

random.shuffle(list_names)
print 'You are winner: < %s >' % (random.choice(list_names))


