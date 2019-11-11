ar = [2,1,3,4]
ar2 = []
ar.sort(reverse=True)
ar2 = ar[:3]
# pr = list(map(lambda x: x, ar[:3]))
# pr = lambda *arr, x : x*x;
# print(pr(ar2[:3],1))

print(ar2[0]*ar2[1]*ar2[2])