# print2d : Print 2d array with readability

[![PyPI version](https://badge.fury.io/py/print2d.svg)](https://badge.fury.io/py/print2d) 

Replacement of `print()` for printing 2d array with readability.

    print2d(mat1, "*" ,mat2, "=", mult)

    [[4.  3.  1.  1. ]  * [[1 2 3]  = [[26.  24.  39. ]  
     [6.  2.  4.  8. ]     [5 2 6]     [64.  84.  98. ]  
     [1.1 6.6 1.5 0.1]]    [2 3 1]     [37.6 20.6 45.2]] 
                           [5 7 8]]  

## Available types

 - Python `list`
 - NumPy `ndarray`
 - PyTorch `Tensor`

## Install

    pip install print2d


## Usage

Import this module 

    from print2d import *

`print2d()` function gets parameter separated with comma(,).

### Python list

    arr1 = [[1,2],[3,4], [5,6]]
    arr2 = [[1, 2, 3], [4, 5, 6]]
    print2d("arr1", arr1, "arr2", arr2)

---
    arr1 [[1, 2]  arr2 [[1, 2, 3]  
          [3, 4]        [4, 5, 6]] 
          [5, 6]]                  

### NumPy ndarray

    np1 = np.array([[1,2],[3,4], [5,6]])
    np2 = np.array([[1, 2, 3], [4, 5, 6]])
    print2d("np1", np1, "np2", np2)

---
    np1 [[1 2]  np2 [[1 2 3]  
         [3 4]       [4 5 6]] 
         [5 6]]        

### PyTorch Tensor

    tc1 = torch.tensor([[1,2],[3,4], [5,6]])
    tc2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print2d("tc1", tc1, "tc2", tc2)

---
    tc1 tensor([[1, 2],  tc2 tensor([[1, 2, 3],  
                [3, 4],              [4, 5, 6]]) 
                [5, 6]])    

### Combination

    arr1 = [[1,2],[3,4], [5,6]]
    np2 = np.array([[1, 2, 3], [4, 5, 6]])
    print2d("arr1", arr1, "np2", np2)

---
    arr1 [[1, 2]  np2 [[1 2 3]  
          [3, 4]       [4 5 6]] 
          [5, 6]]               


