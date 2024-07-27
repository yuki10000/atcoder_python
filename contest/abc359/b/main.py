N = int(input())

a_list = list(map(int, input().split()))

count = 0

for i in range((2 * N) - 2):
    # print(a_list[i], a_list[i+2])
    if a_list[i] == a_list[i+2]:
        count += 1

print(count)