words = ["apple", "bat", "car", "dog"]

# save only those words that has 3 letters in it
print([x for x in words if len(x)==3])

# print evens in the range
print(f"evens :, {[x for x in range(1,10) if x%2==0]}")

# nested list comprehension
print([[x*y for x in range(1,4)] for y in range(1,4)])

#nested loop for tuple

print([(x,y) for x in range(3) for y in range(3)])

# flattening a list
l=[[x*y for x in range(1,4)] for y in range(1,4)]

print([y for x in l for y in x])

# list comprehension with two list
k= [y for x in l for y in x]
j= [x for x in range(1,10)]
# save only those whose sum is greater than 10
res=[x+y for x in k for y in j if x+y>10]
# print(k,"\n",j,"\n",res)

# add element of same index and save only if sum grater than 10
res=[x+y for x,y in zip(k,j) if x+y>10]
print(k,"\n",j,"\n",res)