import random

# 初期の8x8盤面を設定
def initialize_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    # 初期の4つの石をセット
    board[3][3] = board[4][4] = 'O'  # 白
    board[3][4] = board[4][3] = 'X'  # 黒
    return board

# 盤面を表示する関数
def print_board(board):
    print("  0 1 2 3 4 5 6 7")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

# 指定された位置が有効な場所かチェック
def is_valid_move(board, row, col, player):
    if board[row][col] != ' ':
        return False  # すでに石がある場所には置けない

    opponent = 'X' if player == 'O' else 'O'
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    valid = False
    for dr, dc in directions:
        r, c = row + dr, col + dc
        found_opponent = False
        
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] == opponent:
                found_opponent = True
            elif board[r][c] == player and found_opponent:
                valid = True
                break
            else:
                break
            r += dr
            c += dc
    return valid

# 石を置いて、相手の石を挟んでひっくり返す
def make_move(board, row, col, player):
    board[row][col] = player
    opponent = 'X' if player == 'O' else 'O'
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        to_flip = []
        
        while 0 <= r < 8 and 0 <= c < 8:
            if board[r][c] == opponent:
                to_flip.append((r, c))
            elif board[r][c] == player:
                for flip_r, flip_c in to_flip:
                    board[flip_r][flip_c] = player
                break
            else:
                break
            r += dr
            c += dc

# プレイヤーのターンを処理する
def player_turn(board, player):
    print(f"\nプレイヤー（{player}）のターン")
    while True:
        try:
            row, col = map(int, input(f"石を置く場所を選んでください（行 列）: ").split())
            if 0 <= row < 8 and 0 <= col < 8 and is_valid_move(board, row, col, player):
                make_move(board, row, col, player)
                break
            else:
                print("無効な場所です。もう一度選んでください。")
        except (ValueError, IndexError):
            print("無効な入力です。行と列を整数で入力してください。")

# AI（コンピュータ）のターンを処理する
def ai_turn(board, player):
    print(f"\n{player}（AI）のターン")
    valid_moves = [(r, c) for r in range(8) for c in range(8) if is_valid_move(board, r, c, player)]
    
    if valid_moves:
        row, col = random.choice(valid_moves)  # ランダムで有効な位置を選ぶ
        make_move(board, row, col, player)
        print(f"AIは位置({row}, {col})に石を置きました。")
    else:
        print("AIは置ける場所がありません。")

# 勝者判定
def check_winner(board):
    black_count = sum(row.count('X') for row in board)
    white_count = sum(row.count('O') for row in board)
    
    if black_count > white_count:
        return 'X', black_count, white_count
    elif white_count > black_count:
        return 'O', black_count, white_count
    else:
        return '引き分け', black_count, white_count

# ゲームを実行する関数
def play_game():
    board = initialize_board()
    players = ['X', 'O']  # Xが黒、Oが白
    current_player = 0  # 最初は黒（X）
    
    while True:
        print_board(board)
        
        # プレイヤーのターン（手番交代）
        if current_player == 0:
            player_turn(board, players[current_player])
        else:
            ai_turn(board, players[current_player])
        
        # 勝者判定
        winner, black_score, white_score = check_winner(board)
        if winner != '引き分け' and black_score + white_score == 64:
            print(f"\nゲーム終了！{winner}が勝ちました！")
            print(f"黒: {black_score}点、白: {white_score}点")
            break
        
        # ターン交代
        current_player = (current_player + 1) % 2  # 次のプレイヤーに交代

# ゲーム開始
play_game()