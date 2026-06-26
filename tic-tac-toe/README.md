# tic-tac-toe 🎮

a simple tic-tac-toe game that runs in the terminal. you play as **O**, the computer plays as **X** — and the computer always takes the center first, so good luck.

## how to run

make sure you have python installed, then:

```bash
python tictactoe.py
```

## how to play

- the board is numbered 1-9, like this:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

- enter a number to place your move
- first to get 3 in a row (horizontal, vertical, or diagonal) wins
- if the board fills up with no winner, it's a tie

## what's in the code

- `display_board()` — prints the current board state
- `enter_move()` — handles player input with validation
- `make_list_of_free_fields()` — tracks available squares
- `victory_for()` — checks win conditions for any player
- `draw_move()` — computer picks a random free square

## what i learned building this

- working with 2d lists
- input validation with loops
- breaking down logic into functions
- random module for computer moves

---

built while learning python 🐍
