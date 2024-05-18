N = int(input())

ac_list = []
for i in range(N):
    a, c = input().split()
    ac_list.append([a, int(c)])

# 0からac_list-2まで
for i in range(len(ac_list)-1):
    # i+1からac_list-1まで
    for j in range(i+1, len(ac_list)):
        if (ac_list[i][0] > ac_list[j][0] and ac_list[i][1] < ac_list[j][1]):
            # ac_list[j]をリストから消去 
            ac_list.pop(j)
            break
        elif (ac_list[i][0] < ac_list[j][0] and ac_list[i][1] > ac_list[j][1]):
            ac_list.pop(i)
            break

print(ac_list)