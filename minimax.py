from tictactoe import TicTacToe


def getValue(game: TicTacToe) -> int:
    if game.getWinner()==0: return 1
    if game.getWinner()==1: return -1
    return 0

def Minimax(game: TicTacToe):
    if game.isEnded(): return getValue(game)
    value = float('-inf')
    cells = game.getFreeCells()
    for cel in cells:
        g2 = game.copy()
        g2.play(cel[0],cel[1])
        m = Minimax(g2)
        value = max(value,Minimax(g2))
    return value