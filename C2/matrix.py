import numpy as np

class MatrixOps:
    def __init__(self, seed=None):
        # We use a predetermined seed to evaluate correct implementation
        if seed:
            np.random.seed(seed)

        self._matrix = np.random.randint(0,10, size=(10,10))
        self._kernel = np.random.randint(-2,2, size=(3,3))

    def largest_index(self, matrix):
        ''' Make this function return a tuple of the (row, col)
            index of the largest value in the matrix '''
        max_xy = np.where(matrix == matrix.max())
        result = zip(max_xy[0], max_xy[1])
        return max_xy

    def convolve(self, kernel, matrix):
        ''' Make this function return the result of a 2D convolution '''

        return matrix

    def run(self):
        print("Largest index is at ", self.largest_index(self._matrix))
        print("Result of convolution:")
        print(self.convolve(self._kernel, self._matrix))


if __name__ == "__main__":
    # If this file is run directly from the command line, run a test of the program
    m = MatrixOps()


    print("Running with matrix ")
    print(m._matrix)
    print("and kernel ")
    print(m._kernel)

    m.run()
