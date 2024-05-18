N = int(input())

sc_list = []
for i in range(N):
    s, c = input().split()
    sc_list.append([s, int(c)])


def sort_in_dictionary_order(sc_list):
    sorted_sc_list = sorted(sc_list, key=lambda x: x[0])
    return sorted_sc_list


def cauculate_t(sorted_sc_list):
    t = 0
    for i in range(len(sorted_sc_list)):
        t += sorted_sc_list[i][1]
    return t


def calculate_winning_rate(t, N):
    return t % N


def find_winner(sorted_mod_sc_list, winning_rate):
    for i in range(len(sorted_mod_sc_list)):
        if i == winning_rate:
            return sorted_mod_sc_list[i][0]


sorted_sc_list = sort_in_dictionary_order(sc_list)
# print(sorted_sc_list)
t = cauculate_t(sorted_sc_list)
winning_rate = calculate_winning_rate(t, N)
# print(t, winning_rate)
winner = find_winner(sorted_sc_list, winning_rate)
print(winner)
