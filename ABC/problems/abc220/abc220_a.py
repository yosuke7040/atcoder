a,b,c = [*map(int,input().split())]
if (a > c):
	anser = a + (c - (a%c))
else :
	anser = c
if(anser > b):
	anser = -1
print(anser)