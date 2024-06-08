N, M = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))


sorted_list_A = sorted(list_A)
sorted_list_B = sorted(list_B)

is_consecutive = False

current_alphabet = 'none'

for i in range(N+M):
    if len(sorted_list_A) == 0 or len(sorted_list_B) == 0:
        if len(sorted_list_A) > 1:
            is_consecutive = True
        break
    if sorted_list_A[0] < sorted_list_B[0]:
        if current_alphabet == 'A':
            is_consecutive = True
            break
        else:
            current_alphabet = 'A'
            sorted_list_A.pop(0)
    else:
        current_alphabet = 'B'
        sorted_list_B.pop(0)


if is_consecutive:
    print('Yes')
else:
    print('No')
