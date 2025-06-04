nums=[3,1,4,2,5]
fruits=["apple","banana","cherry"]


#------------------
# Indexing &Slicing
#------------------

print(fruits[-1])  # print last value in fruits

print(nums[1:])   # from index 1 to end

print(nums[::-1]) # reverse list 

nums.append(7) # appends 7 at the end of the list
nums.insert(2,9) # adds a value 9 at index 2
nums.remove(1)  # removes the first 1 it gets
nums.sort()
nums.reverse()
print(nums)
#--------------------
#List comprehensions
#--------------------


[print(x) for x in nums]    # print element by element of a list
print([x**x for x in nums])
print([x for x in nums if x%2==0])
