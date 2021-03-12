# print2d : Print 2d array with readability


Replacement of `print()` for printing 2d array with readability.


    print2d(mat1, "*" ,mat2, "=", mult)

    [[4.  3.  1.  1. ]  * [[1 2 3]  = [[26.  24.  39. ]  
     [6.  2.  4.  8. ]     [5 2 6]     [64.  84.  98. ]  
     [1.1 6.6 1.5 0.1]]    [2 3 1]     [37.6 20.6 45.2]] 
                           [5 7 8]]  

### Usage

`print2d()` function gets parameter separated with comma(,).

    print2d(1)
    print2d(1,2,3)
    print2d(1,2,mat1)
    print2d(1,2,mat1,"test str", mat2)

### Example

Below code runs standard python `print()` function and `print2d()` from `print2d`,

    from print2d import *
    import numpy as np
    
    if __name__ == '__main__':
        mat1 = np.array([[4, 3, 1, 1], [6, 2, 4, 8], [1.1, 6.6, 1.5, 0.1]])
        mat2 = np.array([[1, 2, 3], [5, 2, 6], [2, 3, 1], [5, 7, 8]])
        mult = np.matmul(mat1, mat2)
    
        print("======== print2d() ========")
        print2d(mat1, "*", mat2, "=", mult)
        print("======== print() ========")
        print(mat1, "*", mat2, "=", mult)

and the output is as below.

    ======== print2d() ========
    [[4.  3.  1.  1. ]  * [[1 2 3]  = [[26.  24.  39. ]  
     [6.  2.  4.  8. ]     [5 2 6]     [64.  84.  98. ]  
     [1.1 6.6 1.5 0.1]]    [2 3 1]     [37.6 20.6 45.2]] 
                           [5 7 8]]                      
    ======== print() ========
    [[4.  3.  1.  1. ]
     [6.  2.  4.  8. ]
     [1.1 6.6 1.5 0.1]] * [[1 2 3]
     [5 2 6]
     [2 3 1]
     [5 7 8]] = [[26.  24.  39. ]
     [64.  84.  98. ]
     [37.6 20.6 45.2]]


Note that variables are already calculated and stored.

### Install

    pip install print2d
          

    



