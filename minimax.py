def minimax_ab(node, depth = 15, alpha = float("-inf"), beta = float('inf'), is_max= True, player = True, move = [0,0]):
    children = node.available_moves

    if len(children) == 0 or depth == 0:
        return [move, node.boxes[player] - node.boxes[not player]]

    if is_max:
        best_move = []
        best_score = float("-inf")
        for move in children:
            current = node.copy()
            turn = current.move(move,  player)
            temp = minimax_ab(current, depth - 1, alpha, beta, turn, player, move)
            if temp[1] > best_score:
                best_move = move
                best_score = temp[1]
            alpha = max(best_score, alpha)
            if beta <= alpha:
                break
        return [best_move, best_score]
    else:
        worse_move = []
        worse_score = float("inf")
        for move in children:
            current = node.copy()
            turn = current.move(move,  not player)
            temp = minimax_ab(current, depth - 1, alpha, beta, not turn, player, move)
            if temp[1] < worse_score:
                worse_move = move
                worse_score = temp[1]
            beta = min(beta, worse_score)
            if beta <= alpha:
                break
        return [worse_move, worse_score]

