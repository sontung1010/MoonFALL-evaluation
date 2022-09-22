# C1: Game of Life

In the file `game_of_life.py` is the starter code to implementing Conway's game of life in python 3. If you are unfamiliar with this simulation, the set up is as follows.

There is a board made of cells, these cells can be alive (represented with a 1) or dead (0). At the end of each generation all of the cells are updated to reflect their new state based on 3 rules:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

[(More details on the game can be found here)](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Rules)

For this exercise you will implement these update rules in update function in as few operations as possible. In this case we defined as few operations as the quickest operation time. Perform whatever operations and optimizations you deem necessary.

You can add whatever functions you need, just do not change the headers of the existing functions. Feel free to use any outside libraries that do not need to be pip installed (numpy, scipy, etc).