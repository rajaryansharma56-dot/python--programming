def calculate_plants(initial_plants,plants_added,years):
    total=initial_plants

    for i in range(years):
        total=total+plants_added

    return total

initial=int(input("enter initial plants:"))
added=int(input("enter plants added per year:"))
years=int(input("enter number of years:"))

result=calculate_plants(initial,added,years)

print("total plants:",result)
