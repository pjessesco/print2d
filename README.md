# print2d : Print 2d array with readability

[![PyPI version](https://badge.fury.io/py/print2d.svg)](https://badge.fury.io/py/print2d)

Replacement of `print()` for printing 2d array with readability.

    print2d(mat1, "*" ,mat2, "=", mult)

    [[4.  3.  1.  1. ]  * [[1 2 3]  = [[26.  24.  39. ]  
     [6.  2.  4.  8. ]     [5 2 6]     [64.  84.  98. ]  
     [1.1 6.6 1.5 0.1]]    [2 3 1]     [37.6 20.6 45.2]] 
                           [5 7 8]]  

## Available types

 - `numpy.ndarray`
 - `torch.Tensor`

## Install

    pip install print2d


## Usage

`print2d()` function gets parameter separated with comma(,).

## Example

    from print2d import *
    
    import numpy as np
    import torch
    
    if __name__ == '__main__':
        np_arr = np.array([[1,2,3], [4,5,6]])
        torch_tensor = torch.tensor([[1,2], [3,4], [5,6]])
    
        print2d("np_arr :", np_arr, "torch_tensor :", torch_tensor)

---
    np_arr : [[1 2 3]  torch_tensor : tensor([[1, 2],  
              [4 5 6]]                        [3, 4],  
                                              [5, 6]]) 


## Install

    pip install print2d
          

    



