H, W = map(int, input().split())

S_i, S_j = map(int, input().split())

C = []

# 1行あたりW個の要素を持つH行分の入力を受け取る
for _ in range(H):
    row = list(input())
    C.append(row)

X = list(input())

H -= 1
W -= 1
S_i -= 1
S_j -= 1
for x in X:
    if x == "U":
        if S_i > 0 and C[S_i - 1][S_j] != "#":
            S_i -= 1
    elif x == "D":
        if S_i < H and C[S_i + 1][S_j] != "#":
            S_i += 1
    elif x == "L":
        if S_j > 0 and C[S_i][S_j - 1] != "#":
            S_j -= 1
    elif x == "R":
        if S_j < W and C[S_i][S_j + 1] != "#":
            S_j += 1
    # print(x, S_i, S_j)
            
print(S_i+1, S_j+1)  
