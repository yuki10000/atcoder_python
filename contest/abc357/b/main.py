s = input()
s_list = list(s)
# print(s_list)

num_upper = 0
num_lower = 0

for i in range(len(s_list)):
    if s_list[i].isupper():
        num_upper += 1
    else:
        num_lower += 1

if (num_upper > num_lower):
    print(s.upper())
else:
    print(s.lower())

