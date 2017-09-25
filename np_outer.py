#!/usr/bin/env python
# coding=utf-8

import numpy as np

def test_outer():
    a = [1,2,3,4]
    b = [2,3,4,5]
    print("--------a------")
    print(a)
    print("--------b------")
    print(b)
    print("--------outer------")
    print(np.outer(a, b))

def test_outer2():
    a = np.array([1,2,3,4])
    a = a.reshape(2,2)
    b = np.array([2,3,4,5]).reshape(2,2)
    print(a)
    print(b)
    print(np.outer(a, b))

if __name__ == "__main__":
    test_outer()
    test_outer2()
