S_x, S_y = map(int, input().split())
T_x, T_y = map(int, input().split())

x_distance = T_x - S_x
y_distance = T_y - S_y
fee = 0

if y_distance > x_distance:
