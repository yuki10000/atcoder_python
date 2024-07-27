N = int(input())

name_list = []

for i in range(N):
    name_list.append(input())

name_count = 0

for name in name_list:
    if name == "Takahashi":
        name_count += 1

print(name_count)