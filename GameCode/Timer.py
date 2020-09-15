#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:10:34 2019

@author: ruben107
"""

import datetime

class Timer:
    
    def __init__(self, n, s):
        self.t_name = n
        self.t_timer=s

    def print_time(self):
        return(str(datetime.timedelta(seconds=self.t_timer))[2:])
        
    def add_seg(self,s):
        print(self.t_timer)
        self.t_timer+=s
        print(self.t_timer)
    
    def restar_seg(self,s):
        if (self.t_timer-s)>0:
            self.t_timer-=s
        else:
            self.t_timer=0
    