N, Q = map(int, input().split())
A = list(map(int, input().split()))

bk = [map(int, input().split()) for _ in range(Q)]
B, K = [list(i) for i in zip(*bk)]

# print(N, Q)
# print(A)
# print(B)
# print(K)
result = []

for i in range(Q):
    distances = []
    k_i = K[i]
    for j in range(Q):
        distance = [abs(B[i] - a) for a in A]
        distances.append(distance)
    result.append(distances[k_i])

# resultの要素を1行ずつ表示
for r in result:
    print(r)
        


