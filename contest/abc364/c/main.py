N, X, Y = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Aのi番目の要素とBのi番目の要素をリストにもつリストを作成
C = []
for i in range(N):
    C.append([A[i], B[i]])

# CをAの昇順でソートしたものをC_aとする
C_a = sorted(C, key=lambda x: x[0], reverse=True)
index_a = 0
a_sum_a = 0
b_sum_a = 0

# CをBの昇順でソートしたものをC_bとする
C_b = sorted(C, key=lambda x: x[1], reverse=True)
index_b = 0
a_sum_b = 0
b_sum_b = 0

for i in range(N):
    a_sum_a += C_a[i][0]
    b_sum_a += C_a[i][1]
    # print("a_sum_a", a_sum_a), print("b_sum_a", b_sum_a)
    if a_sum_a > X or b_sum_a > Y:
        index_a = i+1
        break
    elif i == N-1:
        index_a = N

for i in range(N):
    a_sum_b += C_b[i][0]
    b_sum_b += C_b[i][1]
    if a_sum_b > X or b_sum_b > Y:
        index_b = i+1
        break
    elif i == N-1:
        index_b = N
        
# print("index_a", index_a)
# print("index_b", index_b)
# print(X, Y)

if index_a < index_b:
    print(index_a)
else:
    print(index_b)