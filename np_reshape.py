#!/usr/bin/env python
# coding=utf-8

import numpy as np

def test_reshape():
    a = np.arange(12).reshape(2,3,2)
    print("----------2-3-2---------")
    print(a)
    print("----------3-2-2---------")
    a = np.arange(12).reshape(3,2,2)
    print(a)
    print("-------------------")
    print("----------2-2-3---------")
    a = np.arange(12).reshape(2,2,3)
    print(a)
    print("----------4-2-3---------")
    a = np.arange(24).reshape(4, 2, 3)
    print(a)
    print("----------2-3-2-3---------")
    a = np.arange(36).reshape(2, 3, 2, 3)
    print(a)

if __name__ == "__main__":
    test_reshape()
