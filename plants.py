
def calculate_plants(initial_plants,plants_per_plant):
    total=initial_plants+initial_plants*plants_per_plant
    return total

initial=int(input("enter initial number of plants :"))
rate=int(input("enter new plants per plant"))

result=calculate_plants(initial,rate)

print("total plants after one year:",result)
