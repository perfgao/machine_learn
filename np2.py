#!/usr/bin/env python
# coding=utf-8

import numpy as np

def test_dot():
    a = np.arange(12).reshape(2,3,2)
    b = np.arange(12, 24).reshape(2,2,3)
    c= np.dot(a,b)
    print ("---------a--------")
    print (a)
    print ("---------b--------")
    print (b)
    print ("---------c--------")
    print (c)
    print ("---------a0--------")
    print (a[0])
    print ("---------b0--------")
    print (b[0])
    print ("---------c00--------")
    c00 = np.dot(a[0], b[0])
    print (c00)
    print ("---------c10--------")
    c10 = np.dot(a[1], b[0])
    print (c10)
    print ("---------c01--------")
    c01 = np.dot(a[0], b[1])
    print (c01)
    print ("---------c11--------")
    c11 = np.dot(a[1], b[1])
    print (c11)



    print ("------------------")
    print (np.dot([2j, 3j], [2j, 3j]))

if __name__ == "__main__":
    test_dot()
