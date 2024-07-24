# pygame template

A simple template for a game loop and a game state manager using the pygame-ce library.

**main.py**

Runs the game loop and calculates delta time. Delta time is passed in as an argument to the state that's currently running. Uses the game state manager class to manage changing of states

**code/logic/managers.py**

Contains the game state manager, sound manager (TBC) and time manager classes. The game state manager can ask for current or previous state and change game state. The time manager calcuates delta time in the main game loop.

*nkw 2024*