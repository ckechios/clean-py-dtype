ls = [1,2,3]

print("multipled list",ls*3)

squared_ls = []

for x in ls:
    squared_ls.append(x**2)

print("Original:", ls)
print("Squared:", squared_ls)

cubed_ls = [x**3 for x in ls]

print("Cubed:", cubed_ls)