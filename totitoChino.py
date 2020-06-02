class TotitoChino:
    def __init__(self,board):
        self.board = board
        self.available_moves = self.listMoves()
        self.boxes = self.update_points()

    # En esta funcion se hace el movimiento
    # Devuelve True si el movimiento cierra al menos un cuadro
    def move(self,movement,player1):
        # Se extrae el movimiento de los posibles movimientos
        # self.available_moves.remove(movement)
        # Dimension del board
        N = 6
        # Variables de control para el turno
        EMPTY = 99
        FILLED = 0
        punteoAntesTurno = 0
        punteoTurno = 0

        acumulador = 0
        contador = 0
        
        ## Se hace el calculo de los puntos en el board sin el movimiento
        for i in range(len(self.board[0])):
            if ((i + 1) % N) != 0:
                if self.board[0][i] != EMPTY and self.board[0][i + 1] != EMPTY and self.board[1][contador + acumulador] != EMPTY and self.board[1][contador + acumulador + 1] != EMPTY:
                    punteoAntesTurno = punteoAntesTurno + 1
                acumulador = acumulador + N
            else:
                contador = contador + 1
                acumulador = 0

        ## Se hace el movimiento
        self.board[movement[0]][movement[1]] = FILLED

        acumulador = 0
        contador = 0

        ## Se calculan los puntos del self.board con el movimiento hecho
        for i in range(len(self.board[0])):
            if ((i + 1) % N) != 0:
                if self.board[0][i] != EMPTY and self.board[0][i + 1] != EMPTY and self.board[1][contador + acumulador] != EMPTY and self.board[1][contador + acumulador + 1] != EMPTY:
                    punteoTurno = punteoTurno + 1
                acumulador = acumulador + N
            else:
                contador = contador + 1
                acumulador = 0
        
        ## Se verifica si se hicieron puntos, si si, cuantos y de quien.
        if punteoAntesTurno < punteoTurno:
            if player1:
                if punteoTurno - punteoAntesTurno == 2:
                    self.board[movement[0]][movement[1]] = 2
                elif punteoTurno - punteoAntesTurno == 1:
                    self.board[movement[0]][movement[1]] = 1
            else:
                if punteoTurno - punteoAntesTurno == 2:
                    self.board[movement[0]][movement[1]] = - 2
                elif punteoTurno - punteoAntesTurno == 1:
                    self.board[movement[0]][movement[1]] = - 1
            return True
        else:
            return False

    # Funcion que devuelve el listado de posibles movimientos:
    ## e.g. si board[i][j]==99 es un movimiento posible
    def listMoves(self):
        moves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 99:
                    moves.append([i,j])
        return moves

    # Funcion que ve si el juego ya termino
    ## Devuelve False si encuentra algun espacion vacio (e.g. board[i][j] == 99)
    def is_over(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 99:
                    return False
        return True

    # Funcion que devuelve una copia del estado del juego
    ## Con esta copia se haran los calculos de los posibles movimientos
    def copy(self):
        totito = TotitoChino(self.board)
        return totito

    # Funcion que calcula los puntos del board:
    ## player 1 = boxes[True] = boxes[1]
    ## player 2 = boxes[False] = boxes[0]
    def update_points(self):
        boxes = [0,0]
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != 99:
                    if self.board[i][j] > 0:
                        boxes[1] += self.board[i][j]
                    else:
                        boxes[0] -= self.board[i][j]
        return boxes

    # Funcion que manda un el primer movimiento posible
    def dumb_move(self):
        return self.available_moves.pop()
        



