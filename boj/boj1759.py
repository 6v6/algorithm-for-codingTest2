import sys
from itertools import combinations
        


input = sys.stdin.readline
l, c = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
comb = combinations(alpha, l)

for sen in comb:
    count = 0
    for letter in sen:
        if letter in vowel:
            count += 1
    
    if count >= 1 and l-count >= 2:
        print(''.join(sen))


