# trail-task.py
## Description
A version of trail-game but implemented in PyGame for porting to Python-native AI Projects.
This is a trail environment for the Santa Fe Trail, John Muir Trail, and arbitrary trail tasks.

## Starting the game
To play the game you must make sure to have the PyGame library installed. You can do so using \
pip: 

```
pip install pygame
```

or Conda:
```
conda install pygame
```
If you have the pygame library installed you may begin the game by calling game.py to the python interpreter.
```
python3 game.py
```

## Usage
To define a trail simply click on the gridspaces you'd like to place a trail 'pellet'.
If you would like to load an experimental trail task you can do so by pressing 's' : santa fe trail (implemented), or 'j' : john muir trail (to be implemented)

### Controls: 
- If using LRM (left, right, move) you may turn the ant left with `j`, or right with `k`, and move the ant forward using `f`
- If using UDLR (up, down, left, right) you may move the ant using the arrow keys on your keyboard
You may quit the game at anytime using the OS exit button, or by pressing `q` on your keyboard

