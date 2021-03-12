# print2d : Print 2d array with readability

[![PyPI version](https://badge.fury.io/py/print2d.svg)](https://badge.fury.io/py/print2d)

Replacement of `print()` for printing 2d array with readability.


    print2d(mat1, "*" ,mat2, "=", mult)

    [[4.  3.  1.  1. ]  * [[1 2 3]  = [[26.  24.  39. ]  
     [6.  2.  4.  8. ]     [5 2 6]     [64.  84.  98. ]  
     [1.1 6.6 1.5 0.1]]    [2 3 1]     [37.6 20.6 45.2]] 
                           [5 7 8]]  

## Install

    pip install print2d


## Usage

`print2d()` function gets parameter separated with comma(,).

## Example

### 2d NumPy array

    from print2d import *
    import numpy as np
    
    if __name__ == '__main__':
        npmat = np.array([[4, 3, 1, 1], [6, 2, 4, 8], [1.1, 6.6, 1.5, 0.1]])
        print2d("This is 2d np array : ", npmat)

---

    This is 2d np array :  [[4.  3.  1.  1. ]  
                            [6.  2.  4.  8. ]  
                            [1.1 6.6 1.5 0.1]] 




## Install

    pip install print2d
          

    



