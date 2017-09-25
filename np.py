import numpy as np

def array1():
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    c = np.array([[1,2,3,4,], [4,5,6,7], [7,8,9,10]])
    print (a, b , c)
    print ("c.dtype: ", c.dtype)
    print ("a.shape: ", a.shape)
    print ("c.shape: ", c.shape)
    print ("a[1:3]: ", a[1:3])
    print ("a[-3:-1]: ", a[-3:-1])
    print ("c[1][1:3]: ", c[1][1:3])

def array2():
    a2 = np.array([1,2,3,4,5,6])
    a2[2:4] = 100, 101
    print (a2)

    b2 = a2[3:7]
    b2[2] = -101
    print (b2)
    print (a2)

def matrix1():
    ma = np.matrix([[1,2,3],[4,5,6]])
    print (ma * ma)
    mb = np.matrix([[1,2], [3, 4]])
    print (2 * mb)

def matrix2():
    ma = np.matrix([[1, 2],[1, -1]])
    mb = np.matrix([[1, 2 , -3], [-1, 1, 2]])
    print (ma)
    print (mb)
    print (ma * mb)

    mc = np.matrix([[1], [2], [3]])
    md = np.matrix([[1,2,3]])
    print (mc * md)

if __name__ == "__main__":
    array1()
    array2()
    matrix1()
    matrix2()
