frequency={}

for i in range(10):
    n=int(input(f"enter number {i+1} :"))

    if n in frequency:
        frequency[n]+=1

    else:
        frequency[n]=1

for number,count in frequency.items():
    print(number,"->",count)
