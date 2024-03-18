def max_prod_fast(arr):
    p1 = max(arr)
    arr.remove(p1)
    p2 = max(arr)
    return p1*p2

lst = []
 
# number of elements as input
n = int(input())
 
# iterating till the range
lst = list(map(int,input().strip().split()))[:n]
# print(lst)
ans = max_prod_fast(lst)
print (ans)
