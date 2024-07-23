# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:26:55 2019

@author: Mathieu
"""

import datetime

def time_until_next_run():
    
    '''
    Calculates number of seconds until next run, at midnight of the next day
    '''
    
    now = datetime.datetime.now()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = datetime.datetime.fromordinal(tomorrow.toordinal())
    time_delta=(tomorrow-now).total_seconds()

    return time_delta