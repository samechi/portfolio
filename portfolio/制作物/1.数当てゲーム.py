import random

# 数当てゲームの関数
def guess_the_number():
    print("数当てゲームへようこそ！1から100の間の数字を当ててください。")
    target_number = random.randint(1, 100)  # コンピュータが選ぶランダムな数
    attempts = 10 # 試行回数

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"{attempt}回目の予想＞ "))
        except ValueError:
            print("数字を入力してください。")
            continue

        # ヒントを表示
        if guess < target_number -10:
            print("小さすぎます！")
        elif guess < target_number  :
            print("少し小さいです！")
        elif guess < target_number:
            print("少し大きいです！")
        elif guess > target_number +10:
            print("大きすぎます！")
        else:
            print(f"正解！{attempt}回目で当たりました！")
            return  # 正解したのでゲーム終了

    # すべての回で当てられなかった場合
    print(f"ゲームオーバー！正解は {target_number} でした。")

# ゲームを再プレイするかどうかを尋ねる関数
def play_game():
    while True:
        guess_the_number()
        play_again = input("もう一度プレイしますか？(y/n): ").strip().lower()
        if play_again != 'y':
            print("ゲームを終了します。Thank you for playing!!")
            break

# ゲームの開始
play_game()