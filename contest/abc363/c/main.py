N, K = map(int, input().split())
S = input()

S = sorted(S)
# Sに存在する文字の種類をカウントし{'a': 3}のような辞書型にする
d = {}
for s in S:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

print(S)
print(d)


