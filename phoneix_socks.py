from collections import Counter

t = int(input())

for _ in range(t):
    n, left_total, right_total = map(int, input().split())
    socks = list(map(int, input().split()))

    left_freq = Counter(socks[:left_total])
    right_freq = Counter(socks[left_total:])

    for color in left_freq:
        if color in right_freq:
            matched = min(left_freq[color], right_freq[color])
            left_freq[color] -= matched
            right_freq[color] -= matched
            left_total -= matched
            right_total -= matched

    if left_total > right_total:
        left_freq, right_freq = right_freq, left_freq
        left_total, right_total = right_total, left_total

    imbalance = (right_total - left_total) // 2
    cost = imbalance

    duplicate_pairs = 0
    for color in right_freq:
        duplicate_pairs += right_freq[color] // 2

    usable_flips = min(imbalance, duplicate_pairs)

    print(cost + (left_total + (imbalance - usable_flips)))
