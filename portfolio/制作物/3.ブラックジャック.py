import random

# カードデッキを作成（ジョーカーなし、Aは1または11として処理）
def create_deck():
    deck = []
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

# カードの点数を計算する
def calculate_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        rank = card[0]
        if rank in ['J', 'Q', 'K']:
            score += 10
        elif rank == 'A':
            score += 11
            ace_count += 1
        else:
            score += int(rank)
    while score > 21 and ace_count:
        score -= 10
        ace_count -= 1
    return score

# ブラックジャックゲーム
def blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("あなたの手札:", player_hand, "点数:", calculate_score(player_hand))
    print("ディーラーの手札: [", dealer_hand[0], ", ? ]")

    while True:
        choice = input("カードを引きますか？（h: ヒット / s: スタンド）＞ ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            print("あなたの手札:", player_hand, "点数:", calculate_score(player_hand))
            if calculate_score(player_hand) > 21:
                print("バースト！あなたの負けです。")
                return
        elif choice == 's':
            break
        else:
            print("無効な入力です。もう一度入力してください。")

    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    print("ディーラーの手札:", dealer_hand, "点数:", calculate_score(dealer_hand))

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21 or player_score > dealer_score:
        print("あなたの勝ちです！")
    elif player_score == dealer_score:
        print("引き分けです！")
    else:
        print("あなたの負けです！")

# ゲームを続けるか確認する関数
def play_game():
    while True:
        blackjack()
        play_again = input("もう一度プレイしますか？（y: はい / n: いいえ）＞ ").lower()
        if play_again != 'y':
            print("ゲームを終了します。Thank you for playing!!")
            break

# ゲームの開始
play_game()