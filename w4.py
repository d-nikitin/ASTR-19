# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:00:53 2022

@author: Dima
"""

class animal:
    arm_len = None
    leg_len = None
    num_eye = None
    tial = False
    furry = False
    
    def __init__(self):
        self.arm_len = 5.5
        self.leg_len = 5.5
        self.num_eye = 2
        self.tail = True
        self.furry = True
        return self
    def __init__(self, arm, leg, eye, tail, furry):
        self.arm_len = arm
        self.leg_len = leg
        self.num_eye = eye
        self.tail = tail
        self.furry = furry
        return self
    
    def print_animal(self):
        print(self.arm_len)
        print(self.leg_len)
        print(self.num_eye)
        print(self.tail)
        print(self.furry)