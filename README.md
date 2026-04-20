# Snake Game

## Description
A Python-based retro arcade application that simulates the classic Snake game using the Pyxel game engine, utilizing grid mechanics, dynamic array management, and a continuous game loop. The Snake game concept was originally invented in 1976 as the arcade game Blockade and was later massively popularized by its inclusion on Nokia mobile phones in 1997. This script captures the essential mechanics of navigating a growing entity to consume targets without colliding with boundaries or itself.

---


## How the Code Works <br>
The game is built around a single SnakeGame class that encapsulates the initialization, state management, and core game loop required for 2D game development.

➤ **Core Game Loop and State Management** : <br>
The application relies on Pyxel's built-in run method, which continuously calls the update and draw functions at a specified frame rate (10 FPS). The game state is maintained using variables for the snake's body (a list of coordinate tuples), the current and queued directional vectors, the apple's location, and the current score.

➤ **Movement and Coordinate Logic** : <br>
The snake's body is represented by a list of grid coordinates, with index 0 acting as the head. During each frame update, a new head position is calculated based on the current directional vector (e.g., (0, -1) for UP). This new head is inserted at the beginning of the list using self.snake.insert(0, new_head). If an apple is not eaten, the last segment of the tail is removed using self.snake.pop(), creating the illusion of forward movement.

➤ **Collision Detection and Interaction** : <br>
Before the snake's position is officially updated, the new head coordinates are checked against the grid boundaries (0 to GRID_W and GRID_H) and the existing segments of the snake's body. If the new head overlaps with a wall or itself, self.game_over is triggered. If the new head matches the apple's coordinates, the score increments, a new apple is spawned, and the tail is not popped, causing the snake to grow longer.

➤ **Input Handling and Queuing** : <br>
Keyboard inputs (pyxel.KEY_UP, KEY_DOWN, etc.) are polled during the update phase. To prevent the player from instantly reversing direction into their own body (e.g., pressing DOWN while moving UP), the code checks the current self.direction before updating the self.next_direction.

---



