#------------------
#For loop
#------------------

# iterate over a range of number 

for i in range(5):
    print(i)
    
    
# iterating over List

l=["apple","banna","cherry"]
for k in l:
    print(k)
    
# iterating over string

for ch in "python":
    print(ch)

#-----------------
# break
#-----------------

for i  in range(5):
    if i == 3:
        break
    print(i)
    
#----------
# continue
#----------

for i in range(5):
    if i ==2:
        continue
    print(i)
    
#--------------
# else clause
#--------------

for i in range(5):
    if i == 5:
        break
    print(i)
else:
    print("Loop completed without a break")
    