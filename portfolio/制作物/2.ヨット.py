import random
from collections import Counter

# サイコロを振る関数
def roll_dice(num_dice=5):
    return [random.randint(1, 6) for _ in range(num_dice)]

# サイコロの目の組み合わせを判定し、得点を計算する関数
def calculate_score(dice):
    score = 0
    counts = Counter(dice)

    if len(counts) == 1:
        print("ヨット！(5 of a Kind)")
        score = 50
    elif 4 in counts.values():
        print("フォー・オブ・ア・カインド (4 of a Kind)")
        score = sum(dice)
    elif 3 in counts.values() and 2 in counts.values():
        print("フルハウス (Full House)")
        score = 25
    elif sorted(dice) in [list(range(1, 6)), list(range(2, 7))]:
        print("ストレート (Straight)")
        score = 40
    elif 3 in counts.values():
        print("スリー・オブ・ア・カインド (3 of a Kind)")
        score = sum(dice)
    elif counts.most_common(1)[0][1] == 2 and len(counts) == 3:
        print("ツーペア (Two Pairs)")
        score = sum(dice)
    else:
        print("チャンス (Chance)")
        score = sum(dice)

    return score

# ヨットゲームを開始する関数
def play_yacht():
    print("ヨットゲームへようこそ！")
    
    # プレイヤーのターン
    dice = roll_dice()
    print("サイコロの出目:", dice)
    
    # 組み合わせを判定してスコアを計算
    score = calculate_score(dice)
    print(f"あなたのスコア: {score}点")

# ゲームを続けるか確認する関数
def play_game():
    while True:
        play_yacht()
        play_again = input("もう一度プレイしますか？（y: はい / n: いいえ）＞ ").lower()
        if play_again != 'y':
            print("ゲームを終了します。Thank you for playing!!")
            break

# ゲームの開始
play_game()