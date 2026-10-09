
print("\n === REFORESTATION ===   ")

def calculate_trees(initial_trees, saplings_per_tree, years):
    mature_trees = initial_trees
    saplings = 0

    for year in range(years):
        mature_trees = mature_trees + saplings
        saplings = mature_trees * saplings_per_tree

    return mature_trees


initial_trees = int(input("Enter initial trees: "))
saplings_per_tree = int(input("Enter saplings per tree: "))
years = int(input("Enter number of years: "))

result = calculate_trees(initial_trees, saplings_per_tree, years)

print("Total mature trees:", result)
