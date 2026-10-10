def calculate_trees(initial_trees,saplings_per_tree,years):
    mature_trees=initial_trees
    new_trees=0

    for i in range(years):
        new_trees=mature_trees*new_trees
        mature_trees=mature_trees+new_trees

    return mature_trees,new_trees

n1=int(input("enter initial number of trees:"))
y1=int(input("enter year:"))
s1=int(input("enter saplings_per_tree"))

result,f1=calculate_trees(n1,s1,y1)

print("total trees:",result)
print("new trees in final year:",f1)
