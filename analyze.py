from tictactoe import TicTacToe
from minimax import Minimax
from random import choice
import matplotlib.pyplot as plt

l = []
N=100

def game(g):
    while not g.isEnded():
        x,y=choice(g.getFreeCells())
        g.play(x,y)
        if not g.isEnded():
            c = Minimax(g)
            g.play(c[0],c[1])
    v = int(g.getWinner()==0)
    return v

for i in range(N):
    l.append(game(TicTacToe()))

plt.plot(l)
plt.show()