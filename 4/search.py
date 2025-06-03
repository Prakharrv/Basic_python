l=[4,3,5,9,6,1,2]

n=int(input("Enter the number you want to search from the list :"))

for idx, val in enumerate(l):
    if val ==n:
        print(f"Found {n} at the index {idx}")
        break
else:
    print(f"{n} is not found in the list")