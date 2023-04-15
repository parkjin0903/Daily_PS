mod = 1000000007
def pow(a,b):
	res = 1
	while b:
		if b & 1:
			res *= a
			res %= mod
		a = a*a
		b >>= 1
		a %= mod
	return res
for _ in range(int(input())):
	N = int(input())
	if N == 1:
		print(1)
	else:
		print(pow(2,N-2))