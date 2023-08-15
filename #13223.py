now = list(map(int, input().split(':')))	# 현재 시간
salt= list(map(int, input().split(':')))	# 소금 투하 시간

# 현재 시간과 소금 투하 시간 초로 환산
now_time = now[0] * 3600 + now[1] * 60 + now[2]
salt_time = salt[0] * 3600 + salt[1] * 60 + salt[2]

if now_time >= salt_time :	# 조건에 해당하면
    salt_time += 24 * 3600	# 24시간의 초를 더함

result = salt_time - now_time	# 경과 시간

hh = str(result // 3600).zfill(2)
mm = str((result % 3600) // 60).zfill(2)
ss = str(result % 60).zfill(2)
print('{}:{}:{}'.format(hh, mm, ss))