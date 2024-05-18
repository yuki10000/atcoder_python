height = int(input())
plant_height = 0
day = 0

while (1):
    if plant_height > height:
        break
    plant_height += 2 ** day
    day += 1

print(day)