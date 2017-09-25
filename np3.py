#!/usr/bin/env python
# coding=utf-8

import numpy as np

def test_inner():
    a = np.arange(12).reshape(2,3,2)
    b = np.arange(12, 24).reshape(2,3,2)
    c = np.inner(a, b)
    print("---------a--------")
    print(a)
    print("---------b--------")
    print(b)
    print("---------c--------")
    print(c)

if __name__ == "__main__":
    test_inner()

