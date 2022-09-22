# C2: Matrix Operations

In the file `matrix.py` is the starter code to implementing two matrix operations: the 2D coordinates of the largest number and the convolution operation. 

For the first task, you must return the row, column index of the largest number in a 2D array. You implementation should be as simple as possible.

For the second task, you must implement the [2D convolution](https://www.allaboutcircuits.com/technical-articles/two-dimensional-convolution-in-image-processing/) operation. In short, the value of each cell of the matrix should be updated to the be sum of all neighboring cells multiplied by the weight for the neighbor as specified in the kernel. The center of the 3x3 kernel will represent the weight applied to cell itself. For cells on the edge, assume the values beyond the border of 0 (zero padding in the article).

You can add whatever functions you need, just do not change the headers of the existing functions. Feel free to use any outside libraries that do not need to be pip installed (such as numpy, scipy, etc).