# MazeGeneration
Maze Generation using Python and Pygames module. My code implements a recursive algorithim to create a path through a matrix and then draws into the Python GUI

The Pseduocode is as follows:

1.Choose next block (direction)
2.Put direction value in current block
3.If next block is empty
  -Repeat algorithim
  Else, if next block is full (out of bounds/has value)
    - check if any other empty directions
    - if so, change direction till an empty one is found
    - if not, go back a block 
