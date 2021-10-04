n = int(input())

s = [""] * n
for i in range(n):
	s[i] = input()

r_cnt = 0
l_cnt = 0

for i in range(n):
	if s[i] == "right":
		r_cnt += 1
	else:
		l_cnt += 1

if r_cnt > l_cnt:
	print("right")
elif r_cnt < l_cnt:
	print("left")
else:
	print("same")