# MazeGeneration
Maze Generation using Python and Pygames module. My code implements a recursive algorithim to create a path through a matrix and then draws into the Python GUI

The Pseduocode is as follows:

1. Choose next block (direction)
1. Put direction value in current block
1. If next block is empty, repeat algorithim
  1. Else, if next block is full (out of bounds/has value)
  1. check if any other empty directions
  1.  if so, change direction till an empty one is found
  1.  if not, go back a block 

NOTE:
- This code is a rough code and needs to be tweaked for little bugs and such that make the maze disconnected in some parts, this will be added further in
