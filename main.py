from tictactoe import TicTacToe
from minimax import Minimax
from random import choice

g = TicTacToe()

while not g.isEnded():
    g.display()
    x = int(input())
    y = int(input())
    print(Minimax(g))
    g.play(x,y)
    if not g.isEnded():
        c = choice(g.getFreeCells())
        g.play(c[0],c[1])

g.display()
if g.getWinner()==-1:
    print("Draw")
else:
    print(f"The winner is {"O" if g.getWinner() else "X"}")