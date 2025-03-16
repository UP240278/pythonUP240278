#01 Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
AB=A.union(B)
print(AB)

#02 Find A intersection B
print(A.intersection(B))

#03 Is A subset of B
print(A.issubset(B))

#04 Are A and B disjoint sets
print(A.isdisjoint(B))

#05 Join A with B and B with A
AB=A.union(B)
BA=B.union(A)
print(AB, BA)

#06 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#07 Delete the sets completely
del A, B, AB, BA