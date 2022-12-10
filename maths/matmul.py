"""¡¡Necesitamos operaciones con matrices!!

A = [[aa, ab],
     [ba, bb]]
X = [[xx, xy],
     [yx, yy]]

MULTIPLICACIÓN:
A @ X = [[aa * xx + ab * yx, aa * xy + ab * yy],
         [ba * xx + bb * yx, ba * xy + bb * yy]]
 
TRASPUESTA:
A.T = [[aa, ba],
       [ab, bb]]
X.T = [[xx, yx],
       [xy, yy]]
"""

A = [[1, 1],
     [2, 1]]

X = [[1, -1],
     [0,  1]]

def matmul(mat1, mat2):
    """
    A @ X = [[ 1,  0],
             [ 2, -1]]
    """
    return mat1 @ mat2 # HAZ AQUÍ TU FUNCIÓN

def transpose(mat):
    """
    A.T = [[ 1,  2],
           [ 1,  1]]
    """
    return mat.T # HAZ AQUÍ TU FUNCIÓN
