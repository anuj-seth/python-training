#!/usr/bin/env python

import datetime
import imp
import sys

class PartyTime(object):
    def __call__(self, *args):
        imp.reload(datetime)
        value = datetime.datetime(*args)
        datetime.datetime = self
        return value

    def __getattr__(self, value):
        if value == 'now':
            return lambda: sys.stdout.write("Party Time!") 
        else:
            imp.reload(datetime)
            value = getattr(datetime.datetime, value)
            datetime.datetime = self
            return value

datetime.datetime = PartyTime()

datetime.datetime.now()

today = datetime.datetime(2017, 04, 14)
print(today)

