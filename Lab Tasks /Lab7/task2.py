def alpha_beta(cards, left, right, is_max, alpha, beta):
    if left > right:
        return 0
    if is_max:
        return max(
            cards[left] + alpha_beta(cards, left + 1, right, False, alpha, beta),
            cards[right] + alpha_beta(cards, left, right - 1, False, alpha, beta)
        )
    else:
        return min(
            alpha_beta(cards, left + 1, right, True, alpha, beta),
            alpha_beta(cards, left, right - 1, True, alpha, beta)
        )

def play_game(cards):
    max_score = 0
    min_score = 0
    left, right = 0, len(cards) - 1
    turn = True  # True = Max

    while left <= right:
        if turn:
            # Max uses alpha-beta pruning
            left_score = cards[left] + alpha_beta(cards, left+1, right, False, float('-inf'), float('inf'))
            right_score = cards[right] + alpha_beta(cards, left, right-1, False, float('-inf'), float('inf'))
            if left_score >= right_score:
                print(f"Max picks {cards[left]}, Remaining: {cards[left+1:right+1]}")
                max_score += cards[left]
                left += 1
            else:
                print(f"Max picks {cards[right]}, Remaining: {cards[left:right]}")
                max_score += cards[right]
                right -= 1
        else:
            # Min picks least value (greedy)
            if cards[left] <= cards[right]:
                print(f"Min picks {cards[left]}, Remaining: {cards[left+1:right+1]}")
                min_score += cards[left]
                left += 1
            else:
                print(f"Min picks {cards[right]}, Remaining: {cards[left:right]}")
                min_score += cards[right]
                right -= 1
        turn = not turn

    print(f"Final Scores - Max: {max_score}, Min: {min_score}")
    print("Winner: Max" if max_score > min_score else "Winner: Min")

cards = [4, 10, 6, 2, 9, 5]
print(f"Initial Cards: {cards}")
play_game(cards)
