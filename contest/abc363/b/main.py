N, T, P = map(int, input().split())

L = list(map(int, input().split()))

# Lの要素がT以上の人がP個以上の時0を出力してプログラムを終了
if sum([1 for i in L if i >= T]) >= P:
    print(0)
    exit()


# for文回しながらLの要素を1ずつ足していき、Lの要素がT以上の人がP個以上になったらその時のiを出力してプログラムを終了
for i in range(1, T+1):
    L = [x + 1 for x in L]
    if sum([1 for j in L if j >= T]) >= P:
        print(i)
        exit()
