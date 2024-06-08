person_list = input().split()
suspect_list = ['1', '2', '3']

for person in person_list:
    if person in suspect_list:
        suspect_list.remove(person)
        # print(suspect_list)

if len(suspect_list) != 1:
    print('-1')
else:
    print(suspect_list[0])
