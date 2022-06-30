x_grid = []
y_grid = []

for _ in range(3):
  a, b = map(int, input().split())
  x_grid.append(a)
  y_grid.append(b)
for i in range(3):
  if x_grid.count(x_grid[i]) == 1:
    answer_x = x_grid[i]
  if y_grid.count(y_grid[i]) == 1:
    answer_y = y_grid[i]

print(answer_x, answer_y)
