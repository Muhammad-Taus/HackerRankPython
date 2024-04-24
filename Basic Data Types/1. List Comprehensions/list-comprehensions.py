xr = range(int(input())+1)
yr = range(int(input())+1)
zr = range(int(input())+1)
n = int(input())

arr = [[i, j, k] for i in xr for j in yr for k in zr if i+j+k != n]
print(arr)
