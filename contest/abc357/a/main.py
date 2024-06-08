N, M = map(int, input().split())
hand_number_list = list(map(int, input().split()))
# print(N, M)

person = N

# print(person)

for i in range(len(hand_number_list)):
    M -= hand_number_list[i]
    if M < 0:
        person = i
        break
    # else:
    #     print("success", hand_number_list[i], M)

print(person)
