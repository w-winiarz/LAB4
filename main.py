import numpy as np
#
# a = np.array([0, 1])
# print(a)
#
#
# a = np.arange(2)
# print(a)
# print(type(a))
#
#
# print(a.dtype)
#
#
# a = np.arange(2, dtype='int32')
# print(a.dtype)
# b = a.astype('float')
# print(b)
# print(b.dtype)
# print(b.shape)
#
#
# # ilosc wymiarow
# print(a.ndim)
#
# m = np.array((np.arange(2), np.arange(2)))
# print(m.shape)
# print(m.ndim)
#
#
# m2 = np.array([[2, 3, 5], [2, 4, 6]])
# print(m2)
# print(m2.shape)
# wektor = np.arange(5)
# print(wektor)
#
# zera = np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
# print(zera.dtype)
# print(jedynki.dtype)
#
# pusta = np.empty((2, 2))
# print(pusta)
# poz_1 = pusta [1, 1]
# poz_2 = pusta[0, 1]
# print(poz_1)
# print(poz_2)
#
# macierz = np.array([[1, 2],
#                     [3, 4]])
# print(macierz)
# liczby = np.arange(1, 2, 0.1)
# print(liczby)
#
# liczby_lin = np.linspace(1, 2, 5, endpoint=False)
# print(liczby_lin)
#
#
# z = np.indices((5, 3))
# print(z)
# print(z[0, 3, 1])
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
#
# # k jak wysoko wektor na przekatnej
# mat_diag_k = np.diag([a for a in range(5)], k=1)
# print(mat_diag_k)
#
# z = np.fromiter(range(5), dtype='int32')
# print(z)
#
# znaki= b'abcdef'
# zn1 = np.frombuffer(znaki,dtype='S1')
# print(zn1)
# zn2 = np.frombuffer(znaki, dtype='S3')
# print(zn2)



# znaki = 'abcdef'
# zn3 = np.array(list(znaki))
# zn4 = np.array(list(znaki), dtype='S1')
# zn5 = np.array(list(b'abcdef'))
# zn6 = np.fromiter(znaki, dtype='S1')
# zn7 = np.fromiter(znaki, dtype='U1')
# print(zn3)
# print(zn4)
# print(zn5)
# print(zn6)
# print(zn7)


# mat = np.ones((2, 2))
# mat_1 = np.ones((2, 2))
# mat = mat + mat_1
# print(mat)
# print(mat - mat_1)
# print(mat * mat_1)
# print(mat / mat_1)
#
#
# mat_1= np.array([[3, 5], [5, 4]])
# print(mat_1)
# print(mat * mat_1)


# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# print(a[2:7:2])
# print(a[1:])
# print(a[2:5])

# mat = np.arange(25)
# mat = mat.reshape((5, 5))
# print(mat)
# print(mat[1:])
# print(mat[:, 1])
# print(mat[:, -1:])
# print(mat[2:5, 1:3])
# print(mat[:, range(2, 6, 2)])
# print('')


x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0,2], [0, 2]])
y = x[rows, cols]
print(y)