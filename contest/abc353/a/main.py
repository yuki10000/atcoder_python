N = int(input())
H = list(map(int, input().split()))
building_number = -1
height = H[0]

for i in range(1, N):
    if (H[i] > height):
        building_number = i+1
        break

print(building_number)
