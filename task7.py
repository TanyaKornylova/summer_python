#analytical solution 0.30555556
import random


def MMC(n):
	count_six = 0
	for i in range(n):
		a = random.randint(1, 6)
		b = random.randint(1, 6)
		if (a == 6 or b == 6):
			count_six += 1
	return count_six / n
	
n = int(input())
analyt_sol = 0.305555
sol = MMC(n)
while abs(sol - analyt_sol) >= 0.0001:
	n = n * 2
	sol = MMC(n)

print(n)
print(sol)
	
