def check_water(ph):
    if ph<7:
        return "Acidic"
    elif ph==7:
        return "Neutral"
    else:
        return "Basic"

ph=float(input("enter ph value:"))

result=check_water(ph)

print("water category:",result)
