# 18-3

N = int(input())

road_list = list(map(int,input().split()))
cost_list = list(map(int,input().split()))

min_price = road_list[0] * cost_list[0]

min_cost = cost_list[0]

for i in range(1, N-1):
  if min_cost > cost_list[i]: 
    min_cost = cost_list[i] 

  min_price += min_cost * road_list[i]

print(min_price)