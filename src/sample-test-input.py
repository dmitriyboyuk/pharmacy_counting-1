#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 00:47:34 2019

@author: a
"""

def sample(file_path, input_file_path, fraction = 0.1):
    
    import random 

    with open(file_path, 'r') as file: 
        lines = file.readlines()        
        N = len(lines)
        n = round(fraction * N) 
        sample = [0]+random.sample(range(1, N-n), n)     
        sample_lines = [lines[i] for i in sample]
    
    with open(input_file_path, 'w') as file:
        for line in sample_lines:
            file.write('%s' % line) 

if __name__ == '__main__':
    sample(file_path= '../input/itcont.txt',input_file_path='../insight_testsuite/tests/my-own-test_1/input/itcont.txt')