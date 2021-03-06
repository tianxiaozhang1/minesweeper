# Minesweeper

Welcome to my Minesweeper exercise.

A game that needs no introduction - Minesweeper is a game from the 1960s and gained popularity since Windows 3.1 in 1992. The Microsoft version was created by Curt Johnson (for IBM's OS/2) and Robert Donner (for Windows).

Only the "Expert" difficulty is implemented for simplicity.

## Features

The rules of this particular version is similar to the Windows version; one minor difference being only flagging/sweeping all mines (and not necessarily opening any other squares) will win the game as well. One added function is to guarantee a successful initial click so the game won't be over before it begins (game will replace the map if a mine is hit upon first click).

In the updated version a self-solving feature is added. The inital click will not only avoid a mine, but will always open up a small area for a smooth experience. This can be implemented for the human player as well.

## Requirements

### Python 3
https://www.python.org/downloads

### Pygame
https://www.pygame.org/wiki/GettingStarted

## [New] Auto-Solving

Tired of all the clicking? The game can solve itself. Using the same info and logic as a human (but very very lucky when a guess is necessary).

![](https://github.com/tianxiaozhang1/minesweeper/blob/main/auto_solve.gif)

![](https://github.com/tianxiaozhang1/minesweeper/blob/main/auto_solve_2.gif)

## Gameplay

![](https://github.com/tianxiaozhang1/minesweeper/blob/main/minesweeper1a.gif)

![](https://github.com/tianxiaozhang1/minesweeper/blob/main/minesweeper2a.gif)

![](https://github.com/tianxiaozhang1/minesweeper/blob/main/minesweeper3a.gif)

![](https://github.com/tianxiaozhang1/minesweeper/blob/main/minesweeper4a.gif)

## Solving Techniques/Patterns

https://minesweeper.online/help/patterns

## JavaScript Version

The same program (classic version) written in JavaScript is here:

https://github.com/tianxiaozhang1/minesweeper_js

## Further Reading

https://dash.harvard.edu/bitstream/handle/1/14398552/BECERRA-SENIORTHESIS-2015.pdf

Thanks for visiting.
