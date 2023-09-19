import chess
import random
import time
import multiprocessing
import timeout_decorator
from chess import Board


def avaliandoPosicao(board, cor):
    if board.is_checkmate():
        if cor == chess.WHITE:
            return -float("inf")
        else:
            return float("inf")
    if board.is_stalemate():
        return 0.0
    else:
        nota = 0
        for square in chess.SQUARES:
            peca = board.piece_at(square)
            if peca is None:
                continue
            if peca.color == chess.WHITE:
                nota += valorPeca(peca)
                nota += avaliandoTabuleiro(peca, square)
            else:
                nota -= valorPeca(peca)
                nota -= avaliandoTabuleiro(peca, square)
    return nota


def valorPeca(peca):
    # print(peca.color)
    if peca.color == chess.WHITE:
        if peca.piece_type == chess.PAWN:
            return 50
        if peca.piece_type == chess.KNIGHT:
            return 160
        if peca.piece_type == chess.BISHOP:
            return 165
        if peca.piece_type == chess.ROOK:
            return 250
        if peca.piece_type == chess.QUEEN:
            return 450
        if peca.piece_type == chess.KING:
            return 1000
    if peca.color == chess.BLACK:
        if peca.piece_type == chess.PAWN:
            return -50
        if peca.piece_type == chess.KNIGHT:
            return -160
        if peca.piece_type == chess.BISHOP:
            return -165
        if peca.piece_type == chess.ROOK:
            return -250
        if peca.piece_type == chess.QUEEN:
            return -450
        if peca.piece_type == chess.KING:
            return -1000


def avaliandoTabuleiro(peca, posicao):
    tipo = peca.piece_type
    posicionamento = []
    if tipo == chess.PAWN:
        if peca.color == chess.WHITE:
            posicionamento = peoesBranco
        else:
            posicionamento = peoesPreto
    if tipo == chess.KNIGHT:
        posicionamento = cavalo
    if tipo == chess.BISHOP:
        if peca.color == chess.WHITE:
            posicionamento = bispoBranco
        else:
            posicionamento = bispoPeto
    if tipo == chess.ROOK:
        if peca.color == chess.WHITE:
            posicionamento = torreBranca
        else:
            posicionamento = torrePreta
    if tipo == chess.QUEEN:
        posicionamento = rainha
    if tipo == chess.KING:
        if peca.color == chess.WHITE:
            posicionamento = reiBranco
        else:
            posicionamento = reiPreto
    return posicionamento[posicao]


historico_de_posicoes = []


@timeout_decorator.timeout(240)  # para ver se execedeu 4 minutos
def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return avaliandoPosicao(board, board.turn)

    legal_moves = list(board.legal_moves)
    if maximizing_player:
        max_eval = -float("inf")
        for move in legal_moves:
            board.push(move)
            eval = alphabeta(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in legal_moves:
            board.push(move)
            eval = alphabeta(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


peoesBranco = [
    10, 10, 10, 10, 10, 10, 10, 10,
    15, 20, 20, -30, -30, 20, 20, 15,
    15, -15, -20, 10, 10, -20, -15, 15,
    10, 10, 10, 30, 30, 10, 10, 10,
    15, 15, 20, 35, 35, 20, 15, 15,
    20, 20, 30, 40, 40, 30, 20, 20,
    60, 60, 60, 60, 60, 60, 60, 60,
    10, 10, 10, 10, 10, 10, 10, 10
]
peoesPreto = list(reversed(peoesBranco))

cavalo = [
    -60, -50, -40, -40, -40, -40, -50, -60,
    -50, -30, 10, 10, 10, 10, -30, -50,
    -40, 10, 20, 25, 25, 20, 10, -40,
    -40, 15, 25, 30, 30, 25, 15, -40,
    -40, 10, 25, 30, 30, 25, 10, -40,
    -40, 15, 20, 25, 25, 20, 15, -40,
    -50, -30, 10, 15, 15, 10, -30, -50,
    -60, -50, -40, -40, -40, -40, -50, -60
]

bispoBranco = [
    -30, -20, -20, -20, -20, -20, -20, -30,
    -20, 15, 10, 10, 10, 10, 15, -20,
    -20, 20, 20, 20, 20, 20, 20, -20,
    -20, 10, 20, 20, 20, 20, 10, -20,
    -20, 15, 15, 20, 20, 15, 15, -20,
    -20, 10, 15, 20, 20, 15, 10, -20,
    -20, 10, 10, 10, 10, 10, 10, -20,
    -30, -20, -20, -20, -20, -20, -20, -30
]
bispoPeto = list(reversed(bispoBranco))

torreBranca = [
    10, 10, 10, 15, 15, 10, 10, 10,
    -15, 10, 10, 10, 10, 10, 10, -15,
    -15, 10, 10, 10, 10, 10, 10, -15,
    -15, 10, 10, 10, 10, 10, 10, -15,
    -15, 10, 10, 10, 10, 10, 10, -15,
    -15, 10, 10, 10, 10, 10, 10, -15,
    15, 20, 20, 20, 20, 20, 20, 15,
    10, 10, 10, 10, 10, 10, 10, 10
]
torrePreta = list(reversed(torreBranca))

rainha = [
    -30, -20, -20, -15, -15, -20, -20, -30,
    -20, 10, 10, 10, 10, 10, 10, -20,
    -20, 10, 15, 15, 15, 15, 10, -20,
    -15, 10, 15, 15, 15, 15, 10, -15,
    10, 10, 15, 15, 15, 15, 10, -15,
    -20, 15, 15, 15, 15, 15, 10, -20,
    -20, 10, 15, 10, 10, 10, 10, -20,
    -30, -20, -20, -15, -15, -20, -20, -30
]

reiBranco = [
    30, 40, 20, 10, 10, 20, 40, 30,
    30, 30, 10, 10, 10, 10, 30, 30,
    -20, -30, -30, -30, -30, -30, -30, -20,
    30, -40, -40, -50, -50, -40, -40, -30,
    -40, -50, -50, -60, -60, -50, -50, -40,
    -40, -50, -50, -60, -60, -50, -50, -40,
    -40, -50, -50, -60, -60, -50, -50, -40,
    -40, -50, -50, -60, -60, -50, -50, -40
]
reiPreto = list(reversed(reiBranco))

while True:
    board = chess.Board()
    escolhaOrdem = input("Escolha entre peças brancas ou pretas para jogar: ")

    if (escolhaOrdem.title() == 'Pretas' or escolhaOrdem.title() == 'Preta'):
        ordem = chess.BLACK
        vezJogador = 0
        vezSistema = 1
        break

    elif (escolhaOrdem.title() == 'Brancas' or escolhaOrdem.title() == 'Branca'):
        ordem = chess.WHITE
        vezJogador = 1
        vezSistema = 0
        break

    else:
        print("Opção inválida")


if (vezJogador == 1 and vezSistema == 0):
    while not board.is_checkmate():
        try:
            if ordem == chess.WHITE:
                # jogador jogando
                board.turn = chess.WHITE
                board.legal_moves

                print("Movimentos possíveis na jogada: ")
                for i in board.legal_moves:
                    print(board.san(i), end=" ")

                print("\n")
                print("Entrada jogador")
                local = input('Informe a sua posicao:')  # AONDE ESTOU
                # PARA ONDE QUERO IR
                entrada = input('Escolha sua jogada (posicao desejada):')

                if "=" in entrada:
                    board.push(entrada)
                if entrada == "O-O":
                    if board.turn == chess.WHITE:
                        board.push("e1g1")
                    else:
                        board.push("e8g8")
                if entrada == "O-O-O":
                    if board.turn == chess.WHITE:
                        board.push("e1c1")
                    else:
                        board.push("e8c8")
                if (len(entrada)) == 5:
                    entrada3 = str(entrada[-3]) + str(entrada[-1])
                    board.push_san(entrada3)
                if (len(entrada)) == 4:
                    board.push_san(entrada)
                if (len(entrada)) == 3:
                    entrada2 = str(entrada[-2]) + str(entrada[-1])
                    deslocamento = str(local) + str(entrada2)
                    board.push_san(deslocamento)
                else:
                    deslocamento = str(local) + str(entrada)
                    board.push_san(deslocamento)
                    historico_de_posicoes.clear()
                if board.can_claim_threefold_repetition():
                    print("Regra de repetição! O jogo termina em empate.")
                    break
                ordem = chess.BLACK
                print("\n  Vez jogador")
                display(board)
                time.sleep(2)

            if ordem == chess.BLACK:
                print('\n  Vez sistema')
                try:
                    best_move = None
                    best_eval = -float("inf")
                    legal_moves = list(board.legal_moves)
                    for move in legal_moves:
                        board.push(move)
                        # Adjust depth as needed
                        eval = alphabeta(
                            board, 3, -float("inf"), float("inf"), True)
                        board.pop()
                        if eval > best_eval:
                            best_eval = eval
                            best_move = move
                        board.push(best_move)
                        display(board)
                        ordem = chess.WHITE
                        time.sleep(2)
                        ordem = chess.WHITE
                except timeout_decorator.TimeoutError:
                    print("Execedeu 4 minutos, perdeuuu!!")
                    break
        except:
            print("Jogada proibida, você perdeu!")
            break

if (vezJogador == 0 and vezSistema == 1):
    while not board.is_checkmate():
        try:
            ordem = chess.WHITE
            if ordem == chess.WHITE:
                print('\n  Vez sistema')
                try:
                    best_move = None
                    best_eval = -float("inf")
                    legal_moves = list(board.legal_moves)
                    for move in legal_moves:
                        board.push(move)
                        # Adjust depth as needed
                        eval = alphabeta(
                            board, 3, -float("inf"), float("inf"), False)
                        board.pop()
                        if eval > best_eval:
                            best_eval = eval
                            best_move = move
                        board.push(best_move)
                        display(board)
                        ordem = chess.WHITE
                        time.sleep(2)
                except timeout_decorator.TimeoutError:
                    print("Execedeu 4 minutos, perdeuuu!!")
                    break

            if ordem == chess.BLACK:
                board.turn = chess.BLACK
                board.legal_moves

                print("Movimentos possíveis na jogada: ")
                for i in board.legal_moves:
                    print(board.san(i), end=" ")

                print("\n")
                print("Entrada jogador")
                local = input('Informe a sua posicao:')  # AONDE ESTOU
                # PARA ONDE QUERO IR
                entrada = input('Escolha sua jogada (posicao desejada):')

                if "=" in entrada:
                    board.push(entrada)
                if entrada == "O-O":
                    if board.turn == chess.WHITE:
                        board.push("e1g1")
                    else:
                        board.push("e8g8")
                if entrada == "O-O-O":
                    if board.turn == chess.WHITE:
                        board.push("e1c1")
                    else:
                        board.push("e8c8")
                if (len(entrada)) == 5:
                    entrada3 = str(entrada[-3]) + str(entrada[-1])
                    board.push_san(entrada3)
                if (len(entrada)) == 4:
                    board.push_san(entrada)
                if (len(entrada)) == 3:
                    entrada2 = str(entrada[-2]) + str(entrada[-1])
                    deslocamento = str(local) + str(entrada2)
                    board.push_san(deslocamento)
                else:
                    deslocamento = str(local) + str(entrada)
                    board.push_san(deslocamento)
                historico_de_posicoes.clear()
                if board.can_claim_threefold_repetition():
                    print("Regra de repetição! O jogo termina em empate.")
                    break
                ordem = chess.WHITE
                print("\n  Vez jogador")
                display(board)
        except:
            print("Jogada proibida, você perdeu o jogo!")
            break

    if board.is_checkmate():
        display(board)
