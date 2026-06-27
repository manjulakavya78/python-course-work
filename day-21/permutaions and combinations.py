from itertools import combinations,permutations
res1=list(combinations('abc',2))
res2=list(permutations('abc',2))
print([''.join(i) for i in res1])
print([''.join(i) for i in res2])
