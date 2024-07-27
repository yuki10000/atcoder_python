N = int(input())

S = []

for _ in range(N):
    S.append(input())
 
can_eat = "Yes"

# 連続してsweetが出てくる場合はNoを出力
for i in range(N-1):
    if S[i] == "sweet" and S[i + 1] == "sweet" and i != N-2:
        can_eat = "No"
        print(can_eat)
        exit()

print(can_eat)
