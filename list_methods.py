numbers=[5,2,1,7,4]
numbers.append(20)#adds 20 to the last index
print(numbers)

numbers.remove(20)#removes what is specified
print(numbers)

numbers.insert(0,10)#(index,character to insert)
print(numbers)

numbers.pop()#removes last character
print(numbers)

print(numbers.index(5))#gives the index of the character specified

print(50 in numbers)#check if 50 is there in list

numbers.insert(4,5)
print(numbers)

print(numbers.count(5))#counts the number of time a character repeats itself

numbers.sort()#sort the list in ascending order
print(numbers)

numbers.reverse()#sort the list in descending order
print(numbers)

numbers2=numbers.copy()
print(numbers)

numbers.clear()
print(numbers)

print(numbers2)

