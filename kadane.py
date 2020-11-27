arr = list(map(int,input().split()))
best,sm = 0,0

for k in range(len(arr)):
	sm = max(arr[k],sm+arr[k])
	best = max(best,sm)

print (best)