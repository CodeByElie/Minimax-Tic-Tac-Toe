from tictactoe import TicTacToe


def getValue(game: TicTacToe) -> int:
    if game.getWinner()==0: return 1
    if game.getWinner()==1: return -1
    return 0

def Minimax(game: TicTacToe,first=True):
    if game.isEnded(): return getValue(game)
    c = None
    if game.getTurn()==0:
        val = float('-inf')
        cells = game.getFreeCells()
        for cel in cells:
            g2 = game.copy()
            g2.play(cel[0],cel[1])
            eval = Minimax(g2,False)
            val = max(val,eval)
            if val==eval: c = cel
    elif game.getTurn()==1:
        val = float('inf')
        cells = game.getFreeCells()
        for cel in cells:
            g2 = game.copy()
            g2.play(cel[0],cel[1])
            eval = Minimax(g2,False)
            val = min(val,eval)
            if val==eval: c = cel
    if first: return c
    return val