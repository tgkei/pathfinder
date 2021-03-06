# pathfinder
## Description
Simple GUI path finder with various algorithms

Based on youtube tutorial (<a href="https://www.youtube.com/watch?v=JtiK0DOeI4A&t=236s" target="_blank">`A* Pathfinding Visualization Tutorial - Python A* Path Finding Tutorial`</a>.)

## Added Features
-  [x] Split files
-  [x] Remove unnecessary variables
-  [x] No path found case is handled
-  [X] Add algorithms
   -  [X] DFS
   -  [X] BFS
-  [ ] Improve A*search (WIP) 
-  [ ] Add button so algorithm can be selected in GUI
-  [X] Using register decorator

*More detail information about changed feature is in **changed** file*

## Example
![Recordit GIF](http://g.recordit.co/QRqe1iCnGT.gif)

## Setup:
```
pip install -r requirements.txt
```
*This requirment is only for mac os. Using pygame version 2.0.0.dev4 due to <a href="https://github.com/pygame/pygame/issues/555" target="_blank">`pygame issue#555`</a>.*
*Other OS can use pygame version 1.9.\**

## How to run
Following command start the program
```
python main.py [-algo=(astar|bfs|dfs)]
```
After the program has started
-  First left mouse click: Start point
-  Second left mouse click : End point
-  After 2nd left mouse click: Barrier
-  Right mouse click: Delete clicked block
-  Space: Start searching path if there is start point and end point
-  r : Reset the program
